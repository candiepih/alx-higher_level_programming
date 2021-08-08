#!/usr/bin/python3
""" script that lists all `State` objects that contain the letter
    `a` from the database `hbtn_0e_6_usa`
"""

from sys import argv
from model_state import Base, State
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
    q = session.query(State).filter(State.name.contains("a%")
                                    ).order_by(State.id).all()
    for row in q:
        print("{}: {}".format(row.id, row.name))
