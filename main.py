from datetime import timedelta

from celery import Celery

import psutil

from database import Base, get_engine, get_session
from models import MemoryLog

celery_app = Celery("__name__")

celery_app.conf.timezone = "UTC"
celery_app.conf.broker_url = "redis://127.0.0.1:6379/1"

celery_app.conf.beat_schedule = {
    "memory_info_task_every_minute": {
        "task": "tasks.memory_info",
        "schedule": timedelta(seconds=2),
    },
}


@celery_app.task(name="tasks.memory_info")
def memory_info():
    memory = psutil.virtual_memory()
    free = memory.free / (1024 ^ 2)
    used = memory.used / (1024 ^ 2)
    total = memory.total / (1024 ^ 2)

    session = get_session()
    log = MemoryLog(free=free, used=used, total=total)
    session.add(log)
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(get_engine(), checkfirst=True)
