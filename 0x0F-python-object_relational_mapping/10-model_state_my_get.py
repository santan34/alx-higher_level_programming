#!/usr/bin/python3
"""intro to alx sql alchemny"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Sasho = sessionmaker(bind=engine)
    session = Sasho()
    found = 0
    for star in session.query(State).order_by(State.id):
        if argv[4] == star.name:
            print("{}".format(star.id))
            found = 1
    if found == 0:
        print("Not found")
