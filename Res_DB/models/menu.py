from peewee import CharField, IntegerField, SmallIntegerField
import  khayyam as jalali
from src.Res_DB.models.basemodel import BaseModel


class Item(BaseModel):
    ITEM_TYPE_CHOICE = (
        ('f', 'food'),
        ('s', 'starter'),
        ('b', 'beverage')
    )
    name = CharField(max_length=32)
    item_type = CharField(max_length=1, choices=ITEM_TYPE_CHOICE)
    price = IntegerField()
    duration = SmallIntegerField()
