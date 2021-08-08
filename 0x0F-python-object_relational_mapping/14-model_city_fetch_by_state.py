#!/usr/bin/python3
""" prints all `City` objects from the database `hbtn_0e_14_usa`
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    Engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password,
                                   db_name), pool_pre_ping=True)
    Base.metadata.create_all(Engine)
    Session = sessionmaker(bind=Engine)
    session = Session()
    q = session.query(State, City).join(City).order_by(City.id).all()
    for row in q:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.close()
