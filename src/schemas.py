from datetime import date
from typing import List
from pydantic import BaseModel


class Create_user(BaseModel):

    name: str
    address: str
    email: str
    phone_number: str
    date_of_birth: date


class User(Create_user):
    id: int

    class Config:
        orm_mode = True


class Create_nr_cluster(BaseModel):

    name: str
    address: str
    city: str
    latitude: str
    longitude: str


class NR_Cluster(Create_nr_cluster):
    id: int

    class Config:
        orm_mode = True


class Create_user_nrcluster(BaseModel):
    user_id: int
    nr_cluster_id: int
    role: str


class User_NRCluster(Create_user_nrcluster):
    id: int

    class Config:
        orm_mode = True
