from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///", echo=True)

Base = declarative_base()


def get_engine():
    return engine


def get_session():
    session_maker = sessionmaker(bind=engine)
    return session_maker()
