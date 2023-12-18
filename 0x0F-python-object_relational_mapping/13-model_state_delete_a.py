#!/usr/bin/python3
"""
    script that deletes all State objects witha
    name containing the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker, declarative_base
from model_state import State, Base

Base = declarative_base()

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.like('%a%'))
    if data is not None:
        for ele in data:
            session.delete(ele)
        session.commit()
