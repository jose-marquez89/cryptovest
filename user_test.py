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
new_user = User(name="Mr. Penguin", password="tux2021")
other_user = User(name="Batman", password="theBat123")
transaction = Ledger(asset="BTC", amount=199.99, user_id=new_user.id)
other_transaction = Ledger(asset="GRT", amount=1232.56, user_id=other_user.id)

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    print(new_user.id, other_user.id)
    to_add = [new_user, other_user]
    session.add_all(to_add)
    print(new_user.id, other_user.id)
    session.commit()
    session.close()

    
