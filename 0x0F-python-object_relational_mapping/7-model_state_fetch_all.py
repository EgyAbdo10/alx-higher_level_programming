#!/usr/bin/python3

"""this is a module to retrieve data from States table in a db"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
        )

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    records_ = session.query(State).order_by(State.id.asc())

    for rec in records_:
        print(f"{rec.id}: {rec.name}")
