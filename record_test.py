import os

import pymysql
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conn_test import User, Ledger

load_dotenv()

DB_UNAME = os.environ["DB_UNAME"]
DB_PWORD = os.environ["DB_PWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]

engine = create_engine(f'mysql+pymysql://{DB_UNAME}:{DB_PWORD}@{DB_HOST}/{DB_NAME}')
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(User).filter(User.name == "Mr. Penguin")


if __name__ == "__main__":
    penguin = query.one()
    password_attempt = "helloWorld"

    print(penguin.password == password_attempt)
    print(penguin.password == "tux2021")

    transaction = Ledger(asset="BTC", amount=199.99, user_id=penguin.id)
    other_transaction = Ledger(asset="GRT", amount=1232.56, user_id=penguin.id)

    entries = [transaction, other_transaction]
    session.add_all(entries)
    session.commit()
    session.close()

    
