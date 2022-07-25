# TODO-4: Add create_time() function which get proper data from user,
#       create Item instance and return
# TODO-4: Add get_order() function which will:
#       get item data from user, create Order intance and return
#       Call show_menu() method of Item class on the top of each order,
#       User can select any item, anytime
#       It's up to you (developer) how to store items(by id, uuid, instance)
# TODO-4: Add show_unpaid_bill() function which will render a list to console
# TODO-4: Add pay_bill() function which just get a bill identifier
#       (id, uuid or ...) and set all related payment flags to True
# TODO-4: Add get_finance_report() method which will show last 10 paid
#       Payments and aggregation of all paid payments as integer (Hint: use
#       paid_list() method of Payment class)
from abc import abstractmethod

from menu import Item
# from khayyam import jalali_datetime
from order import Order
from src.finance import Bill
from store import Store
from lib import FILE_PATH, Manager, ClassBase


class Run_App(ClassBase):

    # @abstractmethod
    # def

    def end_program():
        Store.save_to_file(FILE_PATH, Manager.items_data())
        return '0'

    @classmethod
    def create_obj(cls):
        class_name = {
            '0': Item,
            '1': Order,
            '2': Bill

        }
        index_flg = [i for i in input('Enter The Related class: \n '
                                      '0:Item \t 1:Order \t 2: Bill ** with new or load(0_1):').split()]

        cls.manager.create(class_name[index_flg[0]], bool(int(index_flg[1])))



# @classmethod
# def choose_main(cls):
#     MAIN_MENU = {
#         '0': Run_App.end_program,
#         '1': Manager.show_menu(),
#         '2': Run_App.create_obj(),
#         '3': Order.add_order
#     }
#     return MAIN_MENU[]

from utils import Run_App


def run_main():
    main_menu = {
        '0': Run_App.end_program,
        '1': Manager.show_menu,
        '2': Run_App.create_obj,
        '3': Order.add_order
    }
    cmd = None
    # item  =Item()
    while cmd != '0':
        cmd = input('End Program:0 \t'
                    'Show menu :1  \t'
                    'Create Item :2 \t'
                    'Add Order :3  \t')

        var = main_menu[cmd]()
