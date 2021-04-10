import os
import logging

import flask
import pymysql
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_model import User, Ledger, load_engine

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

load_dotenv()

DB_UNAME = os.environ["DB_UNAME"]
DB_PWORD = os.environ["DB_PWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]

engine = create_engine(f'mysql+pymysql://{DB_UNAME}:{DB_PWORD}@{DB_HOST}/{DB_NAME}')

def create_new_user(username, password):
    """Creates a new user in the database"""
    Session = sessionmaker(bind=engine)
    user_create_session = Session()

    # check if the user exists, this may not be the best way to do this
    try:
        existing = user_create_session.query(User).filter_by(name=username).one()
        logging.debug("existing user error handling triggered")
        user_create_session.close()

        return 1 

    except:
        new_user = User(name=username, password=password)
        user_create_session.add(new_user)
        user_create_session.commit()
        user_create_session.close()

def validate_user(username, password):
    """Checks user entered password against database"""
    Session = sessionmaker(bind=engine)
    login_session = Session()

    # check if the user exists and validate password
    try:
        existing = login_session.query(User).filter_by(name=username).one()

        if password == existing.password:
            login_session.close()

            return 0

        login_session.close()

        return 1

    except:
        logging.debug("User was non-existent")
        login_session.close()

        return -1

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    print(new_user.id, other_user.id)
    to_add = [new_user, other_user]
    session.add_all(to_add)
    print(new_user.id, other_user.id)
    session.commit()
    session.close()

    
