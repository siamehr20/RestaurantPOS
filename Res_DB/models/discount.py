from xmlrpc.client import DateTime

from src.Res_DB.models.basemodel import BaseModel

from peewee import CharField, SmallIntegerField


class Discount(BaseModel):
    code = CharField(max_length=8)
    count = SmallIntegerField()
    start_date = DateTime()
    end_date = DateTime()
    percentage = SmallIntegerField()
    min_order = SmallIntegerField()
    max_order = SmallIntegerField()