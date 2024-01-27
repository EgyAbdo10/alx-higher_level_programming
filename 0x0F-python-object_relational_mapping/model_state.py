#!/usr/bin/python3

"""this is a module to create States table in a db"""

from sqlalchemy import Integer, Null, String, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
Base = declarative_base()


class State(Base):
    """
    this class creates a 'states' table in a passed db
    with the follwoign attrs:
    id: int primary key
    name: the name of the state
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


engine = create_engine(
    f"mysql+mysqlconnector://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )

Base.metadata.create_all(bind=engine)
