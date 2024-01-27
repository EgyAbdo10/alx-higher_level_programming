#!/usr/bin/python3

"""this is a module to retrieve the records from cities table in a db"""

from model_state import Base, State
from model_city import City
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

    records = session.query(State.name.label("s_name"), City.id.label("c_id"),
                            City.name.label("c_name"),).filter(
                            State.id == City.state_id).all()
    for record in records:
        # <state name>: (<city id>) <city name>
        print(f"{record.s_name}: ({record.c_id}) {record.c_name}")
