# TODO-1: Add Item class here
# TODO-1: Add .sample() classmethod for Item which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)

import datetime
import time
import uuid
from khayyam import jalali_datetime, JalaliDatetime
from abc import abstractmethod
from lib import ClassBase, Manager
from lib import ClassBase, Manager



class Item(ClassBase):
    item_list = []
    food_list = []
    belevage_list = []
    starter_list = []
    items_counts = 0


    def __init__(self,time,_id, item_id, name, item_type, price,datetime=None):
        # super().__init__(**kwargs)
        self._id = _id
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.price = price
        self.time = time
        self.datetime = datetime
        Item.item_list.append(self)
        self.add_to_related_list(self.item_type)
        self.introduce_class_name(type(self))
        self.manager.save_data(type(self),self)


    def add_to_related_list(self, item_type):
        if item_type == 'f':
            Item.food_list.append(self)
        elif item_type == 'b':
            Item.belevage_list.append(self)
        else:
            Item.starter_list.append(self)

    @classmethod
    def get_item_id(cls):
        cls.items_counts += 1
        return cls.items_counts

    # @classmethod
    # def uuid_generator(cls):
    #     return cls.uuid

    @classmethod
    def prompt(cls, **kwarg):
        cls.name = input('Enter The Item name: ')
        cls.item_type = input('Enter Item Type(f,b,s): ')
        cls.price = input('Enter Item Price: ')
        cls.time = input('Enter The Time To prepare item: ')
        cls.item_id = cls.get_item_id()

        result = {
            '_id': uuid.uuid4().hex, 'name': cls.name,
            'item_id': cls.item_id, 'item_type': cls.item_type,
            'price': cls.price, 'time': cls.time,
            'datetime': JalaliDatetime.now().strftime('%C')
        }

        return result

    @staticmethod
    def add_item():
        items = Item.prompt()
        item = Item(**items)
        return item

    def serializer(self):
        items_data = self.__dict__
        return items_data

    @classmethod
    def items_data(cls):
        itemslist = []
        for item in cls.item_list:
            itemslist.append(item.serializer())
        return itemslist



    @property
    def _jalali_datetime(self):
        return self.JalaliDatetime(datetime.datetime.now())

    @classmethod
    def search(cls, uuid=None, item_id=None, name=None):
        temp_id = uuid
        if uuid == None:
            temp_id = item_id
        else:
            temp_id = name
        for item in cls.item_list:
            if temp_id in [item.uuid, item.item_id, item.name]:
                return item
        return None

    @abstractmethod
    def introduce_class_name(self, type_obj):
        # parrent_class = self.__class__
        if type_obj not in Manager.class_list :
            return self.manager(type_obj)

    @classmethod
    def sample(cls):
        return cls(_id=uuid.uuid4().hex,item_id='1', name='pizza', item_type='f', price='25,000', time="15\'")

    @classmethod
    def sample1(cls):
        return cls(_id=uuid.uuid4().hex,item_id='2', name='pasta', item_type='f', price='55,000', time="20\'")

    @classmethod
    def db_initial(self,**kwargs):
        from Res_DB.models.menu import Item
        Item(**kwargs)
# Item.sample()
items = Item.prompt()
Item.db_initial(**items)
# Manager.save_data(Item,item1)
# Manager.load_data(Item)
# from src.order import Order
# TODO-2: Add item_id to the Item class, item_id should be auto incremental
# TODO-2: item_types should be one of (f, s or b) for Food, Starter or Beverage
# TODO-2: Change datetime attr to be assigned automatically in Item class
# TODO-2: Add jalali_datetime property to the Item class
# TODO-3: Add show_menu() classmethod to the Item class which will print all
#       items in the menu
# TODO-3: Add prompt() method to the Item class which will get proper dict for
# creating each single item from user input and return data
