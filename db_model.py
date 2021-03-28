import os

import pymysql
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, Float, ForeignKey


def load_engine():
    """Create the database engine"""
    load_dotenv()
    
    DB_UNAME = os.environ["DB_UNAME"]
    DB_PWORD = os.environ["DB_PWORD"]
    DB_HOST = os.environ["DB_HOST"]
    DB_NAME = os.environ["DB_NAME"]
    
    engine = create_engine(f'mysql+pymysql://{DB_UNAME}:{DB_PWORD}@{DB_HOST}/{DB_NAME}')

    return engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String(32), unique=True)
    password = Column(String(32))
    transaction = relationship("Ledger")

    def __repr__(self):
        return "<User(name={}, password={}>".format(self.name, self.password)

class Ledger(Base):
    __tablename__ = 'ledger'
    
    id = Column(BigInteger, primary_key=True, nullable=False)
    asset = Column(String(5))
    amount = Column(Float)
    user_id = Column(BigInteger, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<Ledger(asset={}, amount={}, user_id={})>".format(self.asset, self.amount,self.user_id)


if __name__ == "__main__":
    engine = load_engine()
    Base.metadata.create_all(engine)
