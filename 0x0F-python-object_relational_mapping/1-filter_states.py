#!/usr/bin/python3

"""this modules filters all the states' names starting with N"""


import MySQLdb
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", user=argv[1],
                              passwd=argv[2], db=argv[3], port=3306)
    engine = create_engine("mysql+mysqldb://", creator=lambda: db_conn)

    metadata = MetaData()
    States = Table("states", metadata, autoload_with=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(States).filter(
        func.substring(States.c.name, 1, 1) == "N"
        )

    for rec in records:
        # if rec.name[0] == "N":
        print(f"({rec.id}, '{rec.name}')")
    session.close()
