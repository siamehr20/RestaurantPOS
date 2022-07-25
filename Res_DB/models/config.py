from peewee import *


class DataBase():

    def __init__(self):
        self.db = MySQLDatabase(
            'Respos', user = 'siamehr', passwd='Password'
            , host = 'localhost', port = 3306
        )

    def connect(self):
        self.db.connect()
        return self.db


database = Database()
database.connect()