# TODO-1: Add Table class here
# TODO-1: Add .sample() classmethod for Table which returns  an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
from src.lib import ClassBase


class Table(ClassBase):
    free_table_list = []

    def __init__(self,name,number):
        self.name = name
        self.number = number
        Table.free_table_list.append(number)


    @classmethod
    def sample(cls):
        return cls(name = 'Tb1' , number = '1')