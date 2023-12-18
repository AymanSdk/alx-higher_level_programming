#!/usr/bin/python3
"""
python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import State

Base = declarative_base()


if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.like('%a%'))
    for d in data:
        print(d)
