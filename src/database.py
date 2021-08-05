from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgres+psycopg2://delokbwrpzirgy:08feaf754542d4ce0a7a553475b6abfc431909084891ed328502de1112e8f2ef@ec2-54-196-65-186.compute-1.amazonaws.com:5432/damigk5alv2cbj", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
