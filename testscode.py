import datetime
import uuid


class tests:
    counter = 0
    class_list =[]

    def __init__(self,name, age):
        self.name = name
        self.age = age
        type(self).counter+=1
        tests.class_list.append(self)

    def show_counter():
        return tests.counter


# tests_dic = {'name':'siavash' , 'age': '22'}
#
# items = tests(**tests_dic)

# datetime.datetime.fromtimestamp()


inp = input()




# def get_input(self):
#     tup_item = tuple( int(x) for x in inp.split())
#     item_name = input('name').order_loop(True)




items = {'item_name' : 21 , 'name':'mehrad'}


# def get_info():
#         _in = int(input('enter'))
#         yield _in
#
# counter=0
# flg = True
# while flg :
#     if counter==0:
#         print('**** WELCOME TO ADD NEW ORDER ****')
#         nx = get_info()
#         next(nx)
#         counter+=1
#     else:
#         flg = bool(int(input('***Add New Item?!')))
#         if not flg :
#             continue
#         nx = get_info()
#         next(nx)

# id =uuid.uuid4


