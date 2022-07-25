
from peewee import MySQLDatabase, Model, ForeignKeyField, IntegerField\
                , SmallIntegerField, BooleanField, DateTimeField, \
                BigIntegerField

db = MySQLDatabase('Respos',user = 'siamehr',passwd='Password',host = 'localhost',port = 3306)


class BaseModel(Model):
    id = BigIntegerField(primary_key=True)

    class Meta:
        database = db


class Payment(Model):
    payment_type = SmallIntegerField()
    datetime = DateTimeField()
    price = IntegerField()
    is_paid = BooleanField()

    class Meta:
        database = db


class Bill(Model):
    total_price = IntegerField()
    payment = ForeignKeyField(Payment,backref='bill')



if '__name__'=='__main__':
    db.connect()
    db.create_tables([Bill,Payment])

