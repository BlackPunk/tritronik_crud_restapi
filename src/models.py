from typing import Text
from sqlalchemy import Text, Column, ForeignKey, Integer, String, Date
from .database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True,)
    name = Column(String(length=64), nullable=False,)
    address = Column(Text)
    email = Column(String(length=64))
    phone_number = Column(String(length=16))
    date_of_birth = Column(Date)


class Nr_cluster(Base):
    __tablename__ = "nr_cluster"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=64))
    address = Column(Text)
    city = Column(String(length=32))
    latitude = Column(String(length=32))
    longitude = Column(String(length=32))


class User_NRCluster(Base):
    __tablename__ = "user_nrCluster"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    nr_cluster_id = Column(Integer, ForeignKey("nr_cluster.id"))
    role = Column(String(length=32))
