# TODO-5: Create app main loop with the following key options:
#       o: Create new order
#       l: Show list of un paid bills
#       p: Pay one bill by (your preferred) key
#       r: Reset current loop, for example if is inside create order
#            should reset and start loop again
#       e: Exist from current loop, for example step out from create_order
#            to the main menu
#       esc: Close program
# Note: Be careful of user inputs, you should accept L instead of l, E instead
# of e or ...


from menu import Item
# from khayyam import  jalali_datetime
from finance import Bill
from lib import *
from utils import run_main
from order import Order


def run_test():
    order1 = Order.sample()
    print(order1.uuid)
    Order.manager.search(Order,uuid=order1.uuid)

if __name__ == '__main__':

    # run_test()
    run_main()




    print('ss')
