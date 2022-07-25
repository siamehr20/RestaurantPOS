import datetime
import datetime as dt
from peewee import Model, DateTimeField
from src.Res_DB.models.config import db
import  khayyam as jalali


class BaseModel(Model):
    created_datetime = DateTimeField(default=jalali.JalaliDatetime.now())
    modified_time = DateTimeField(default=jalali.JalaliDatetime.now())

    class Meta:
        database = db

    def save(self, force_insert=False, only=None):
        self.modified_time = jalali.JalaliDatetime.now()
        return super().save(force_insert, only)