#!/usr/bin/python3
"""changes the name based on index"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    db = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    sasho = Session()    
    state = sasho.query(State).filter(State.name.like('%a%')).all()
    for name in state:
        sasho.delete(name)
    sasho.commit()
