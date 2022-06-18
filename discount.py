# TODO-2: Add Discount class here

from datetime import datetime


class Discount:
    _code_list = []
    code_dict = {}

    def __init__(self, min_order, code, amount, datetime, item_id, expire='21'):
        self.min_order = min_order
        self.percentage_type = True
        self.code = code
        self.amount = amount
        self.datetime = datetime
        self.expire = expire
        self.item_id = item_id
        Discount._code_list.append(self)

    @classmethod
    def prompt(cls):
        cls.code = input('Enter the Discount code: ')
        cls.min_order = input('Enter Amount of Min Order: ')
        cls.amount = input('Enter Amount Of Discount: ')
        # cls.expire = input('Enter The Expire Date: ')
        cls.item_id = input('Enter The Item Id(s): ')

        result = {'min_order': cls.min_order, 'code': cls.code,
                  'amount': cls.amount, 'item_id': cls.item_id, 'datetime': datetime.now()}

        return result

    @classmethod
    def add_new_code(self):
        code = Discount.prompt()
        generate = Discount(**code)
        # Discount.code_dict.
        token = code['code']
        amount = code['amount']
        Discount.code_dict[token] = amount

    pass
