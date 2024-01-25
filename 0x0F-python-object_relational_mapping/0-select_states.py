#!/usr/bin/python3
"""
this code retrieves data from a states table
in the follwoign format (id, name_of_state)
using sqlalchemy
"""


from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import MySQLdb
from sys import argv

if __name__ == "__main__":


    db_conn = MySQLdb.connect(host="localhost", user=argv[1],
                            passwd=argv[2], db=argv[3], port=3306)

    engine = create_engine("mysql+mysqldb://", creator=lambda: db_conn)
    metadata = MetaData()
    States = Table("states", metadata, autoload_with=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    records = session.query(States).order_by(States.c.id.asc()).all()

    for rec in records:
        print(f"({rec.id}, '{rec.name}')")
    session.close()
    db_conn.close()