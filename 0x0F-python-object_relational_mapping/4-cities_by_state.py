#!/usr/bin/python3

"""
this modules filters all the cities with their states
"""

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", user=argv[1],
                              passwd=argv[2], db=argv[3], port=3306)
    cur = db_conn.cursor()
    # engine = create_engine("mysql+mysqldb://", creator=lambda: db_conn)
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # metadata = MetaData()
    # States = Table("states", metadata, autoload_with=engine)
    # Citeies = Table("cities", metadata, autoload_with=engine)
    cur.execute("""SELECT c.id, c.name, s.name FROM cities as c
                    join states as s
                    on s.id = c.state_id""")
    # records = session.query(Citeies.c.name.label("city_name"),
    #                         Citeies.c.id.label("city_id"),
    #                         States).filter(Citeies.c.state_id == States.c.id)
    records = cur.fetchall()
    for rec in records:
        # print("({}, '{}', '{}')".format(
        # rec.city_id, rec.city_name, rec.name))
        print(rec)
    # session.close()
