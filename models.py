from datetime import datetime

from database import Base
from sqlalchemy import Column, REAL, Sequence, DateTime


class MemoryLog(Base):
    __tablename__ = "memory_logs"

    id = Column(REAL, Sequence("memory_info_seq"), primary_key=True)
    total = Column(REAL)
    used = Column(REAL)
    free = Column(REAL)
    logged_at = Column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return self.id


