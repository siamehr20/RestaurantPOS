# TODO-1: Add Order model here
# TODO-1: Add .sample() classmethod for Order which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
# TODO-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
# TODO-2: Add jalali_datetime property to the Order class
# TODO-2: uuid and datetime attrs should be assigned automatically
# TODO-2: Store a list of orders and a list for un_paid_orders
# TODO-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order
# TODO-2: Add assign_table method to the Order class which assign table to the
#       client and change the table status
# TODO-2: Set I/O for in_out option in Order cfrlass
import uuid
from abc import abstractmethod
from datetime import datetime
import khayyam
from pymongo import MongoClient
from lib import ClassBase, Manager
from finance import Bill
import khayyam

from src.saloon import Table


class Order(ClassBase):
    order_list = []
    paid_orders = []
    unpaid_orders = []

    def __init__(self, _id, item_dict, _in=True, table_number=None, datetime=None):
        self._id = _id
        self.item_dict = item_dict
        self._in = _in
        self.table_number = table_number
        self.datetime = khayyam.jalali_datetime.datetime.now().strftime('%C')
        self.bill = self.set_bill(self._id)
        self.introduce_class_name(type(self))
        self.manager.save_data(type(self), self)
        Order.order_list.append(self)
        Order.unpaid_orders.append(self)

    @classmethod
    def get_items_info(cls):
        from menu import Item
        order_item_list = []
        item_id = (input('Enter The Item_id or uuid: '))
        number = (input('Enter Number of Item: '))
        item = cls.manager.search(Item, item_id=item_id)
        order_item_list = [item, number]
        yield order_item_list
        # flag = change_flag

    @classmethod
    def coutinue_getting_order(cls):
        item_dict = {}
        # counter=0
        flg = True
        while flg:
            # if counter == 0:
            # print('**** WELCOME TO ADD NEW ORDER ****')
            nx = cls.get_items_info()
            item = next(nx)
            item_dict.update(eval(item[0].name), {item[1]: item[0].price})

            flg = bool(int(input('***Add New Item?!')))
            if not flg:
                continue
            nx = cls.get_items_info()
            item_number = next(nx)
            item_dict.update(item[0].name, {item[1]: item[0].price})
        return item_dict

    # def generate_item_dict(self, item_tup: tuple):
    #     uuid = item_tup[0]
    #     number = item_tup[1]
    #     item_name = Item.search(uuid, number).name
    #     item_price = Item.search(uuid, number).price
    #     items_dict = {item_name: { number : item_price}}
    #     return items_dict

    @classmethod
    def prompt(cls):
        print('**** WELCOME TO ADD NEW ORDER ****')
        cls.item_dict = cls.coutinue_getting_order()
        cls._in = bool(int(input('Enter in or not(1_0) ')))
        if cls._in:
            cls.table_number = input('Enter Table Number: ')
        else:
            cls.table_number = None

        result = {
            'item_dict': cls.item_dict, '_id': uuid.uuid4().hex,
            '_in': cls._in, 'table_number': cls.table_number
        }

        return result

    @classmethod
    def add_order(cls):
        orders = cls.prompt()
        order = Order(**orders)
        return order

    @abstractmethod
    def introduce_class_name(self, type_obj):
        if not isinstance(self.manager, Manager):
            self.manager(type_obj)

    def total_price(self):
        for item_name in self.item_dict:
            item_obj = Item.search(item_name)
            self.total_price = item_obj.price * self.item_dict[item_name]
        return self.total_price

    def set_bill(self, order_uuid):
        return Bill(self.total_price, order_uuid, self.item_dict)

    def assign_table(self):
        try:
            index = Table.free_table_list.index(self.table_number)
            Table.free_table_list.pop(index)
        except ValueError:
            print('This Table number is not Free, Choose Another one.!')

    @abstractmethod
    def introduce_class_name(self, type_obj):
        if type_obj not in Manager.class_list:
            return self.manager(type_obj)

    def serializer(self):
        return self.__dict__

    @classmethod
    def sample(cls):
        return cls(_id=uuid.uuid4().hex, item_dict=[], _in=0, table_number=None)


order1 = Order.prompt()
# Order.manager.load_data(Order)
# order1 = Order.init_by_load()
pass
