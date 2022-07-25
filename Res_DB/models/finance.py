from peewee import ForeignKeyField, IntegerField, SmallIntegerField, BooleanField, DateTimeField

from basemodel import BaseModel


class Payment(BaseModel):
    payment_type = SmallIntegerField()
    price = IntegerField()
    is_paid = BooleanField()


class Bill(BaseModel):
    total_price = IntegerField()
    payment = ForeignKeyField(Payment,backref='bill')