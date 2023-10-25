#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from main import (Area, Equipment, User)

if __name__ == '__main__':
    engine = create_engine("sqlite:///main.db")
    session = Session(engine, future=True)


    import ipdb; ipdb.set_trace()