import uuid

from src.Res_DB.models.basemodel import BaseModel
from peewee import CharField, SmallIntegerField, ForeignKeyField, ManyToManyField
from finance import Bill
from menu import Item
from saloon import ResTable
from finance import Bill


class Order(BaseModel):
    ORDER_TYPE_CHOICE = (
        (0,'Inbound') ,
        (1,'Outbound')
    )
    # id = CharField(default=uuid.uuid4().hex)
    order_type = SmallIntegerField(choices=ORDER_TYPE_CHOICE)
    bill = ForeignKeyField(Bill, unique=True, backref='orders')
    table = ForeignKeyField(ResTable, backref='orders')
    item = ManyToManyField(Item, backref='orders')


# class OrderItems(BaseModel):
#     order = ForeignKeyField(Order, backref='items')
#     item = ForeignKeyField(Item, backref='orders')
#     count = SmallIntegerField()