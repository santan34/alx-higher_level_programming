#!/usr/bin/python3
"""intro to alx sql alchemny"""

from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import session, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """a state orm to db

    Args:
        Base (_type_):  function inherited from
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
