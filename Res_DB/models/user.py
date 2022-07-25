
from src.Res_DB.models.basemodel import BaseModel

from peewee import CharField


class Supervisor(BaseModel):
    username = CharField(max_length=16)
    password = CharField(max_length=32)
    phone = CharField(max_length=11, null=True)