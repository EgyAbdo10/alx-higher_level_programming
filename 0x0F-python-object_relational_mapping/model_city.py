#!/usr/bin/python3

"""
this is a module to create States table in a db
and it connects to a databse throw orm sqlalchemy
"""

from sqlalchemy import Integer, Null, String, create_engine, Column, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import State, Base


class City(Base):
    """
    this class creates a 'cities' table in a passed db
    with the follwoign attrs:
    id: int primary key
    name: the name of the state
    state_id: as a foreign key
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))

    def __init__(self, name, state_id, nullable=False):
        self.name = name
        self.state_id = state_id


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqlconnector://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
        )

    Base.metadata.create_all(bind=engine)
