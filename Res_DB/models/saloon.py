from basemodel import BaseModel

from peewee import SmallIntegerField, BooleanField


class ResTable(BaseModel):
    capacity = SmallIntegerField()
    number = SmallIntegerField()
    reserved = BooleanField(default=False)
    is_available = BooleanField(default=True)