# TODO-1: Add Bill class here
# TODO-1: Add .sample() classmethod for Bill and Payment which returns

# TODO-1: Add Payment class here
# an instance:
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
#       to get from input
# TODO-2: Change datetime attr to be assigned automatically in Payment class
# TODO-2: Add jalali_datetime property to the Payment class
# TODO-3: Set valid Payment instance for payment attr in Bill instance
# TODO-3: Add show_unpaid() classmethod to the Bill class which will return a
#       list of all unpaid bills, (Implementation is up to you)
# TODO-3: Add show_paid() classmethod to the Bill as show_unpaid() method
# TODO-3: Add paid_list() classmethod to the Payment class which will just
#       return a list of payments with True `is_paid` flag.
# TODO-3: Add pay() method to the Payment class which set is_paid flag True
# TODO-3: Add total_paid() classmethod to the Payment class which return an int

import uuid
from khayyam import JalaliDatetime
from lib import ClassBase, Manager
from abc import abstractmethod

class Bill(ClassBase):
    bill_list = []
    bill_dict = {}
    unpaid_list = []

    def __init__(self,_id, total_price, order_uuid,pay_status=False,datetime=None):
        self._id = _id
        self.order_uuid = order_uuid
        self.pay_status = pay_status
        self.total_price = total_price
        self.datetime = JalaliDatetime.now().strftime('%C')
        Bill.bill_list.append(self)
        # self.item_dict = item_dict
        # self.payyment = self.create_payment(order_uuid , total_price)
        self.introduce_class_name(type(self))
        self.manager.save_data(type(self),self)

    @abstractmethod
    def introduce_class_name(self, type_obj):
        if type_obj not in Manager.class_list:
            return self.manager(type_obj)
        # return _class_name

    def serializer(self):
        return self.__dict__

    def create_payment(self, bill_uuid, total_price):
        Payment()

    @classmethod
    def show_unpaid(cls):
        if len(cls.unpaid_list) != 0:
             return cls.unpaid_list
        else:
            print('There is No Payment ..!')

    @classmethod
    def sample(cls):
        return cls(total_price='50000', order_uuid='544545', _id=uuid.uuid4().hex)



class Payment(ClassBase):
    payment_list = []

    def __init__(self,_id, bill_uuid,total_price):
        self._id = _id
        self.bill_uuid = bill_uuid
        self.total_price = total_price

# Bill.sample()
Manager.load_data(Bill)
pass
