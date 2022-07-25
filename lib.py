# TODO-3: Create Manager class which has _class attr and search() method
# TODO-3: Implement complete search method functionality in the way you prefer
# TODO-3: `_class` attr in manager is type of composite class
# TODO-3: Add Root class and set manager class_attr None in it
# TODO-3: Add set_manager() method to the Root which set type of self to the
#       `_class` attr of instance manager

# TODO-3: Change sample() method all over your code as follows:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls, name='ali', number=10):
#             return cls(name=name, number=number)
# TODO-3: Add <class-name-lowercase>_list class_attr to the all classes except
#       Manager() and Root() classes


from abc import abstractmethod
import khayyam
import json
from pymongo import MongoClient

FILE_PATH = '/home/siamehr/PycharmProjects/ResturantPOS/src/resturantPOS/__fixtures/items_list'


class Manager:
    class_list = []
    obj_dict = {}
    flag = False

    def __init__(self, _class):

        self._class = _class
        Manager.class_list.append(_class)
        Manager.obj_dict[_class] = self

    def create(class_self, load_flg=False):
        if load_flg:
            Manager.load_data(class_self)
        else:
            class_self.prompt()


    def search_by_db(class_self,**kwargs):
        # cls_name = class_self.__name__ +'s'
        client = MongoClient()
        cls_collection = class_self.__name__ + 's'
        with client:
            keys_list = list(kwargs.keys())
            for key in keys_list:
                value = kwargs[key]




    def search(class_self, **kwargs):
        cls_objs_list = None
        cls_name = class_self.__name__
        cls_objs_list_str = cls_name.lower() + '_list'

        keys_list = list(kwargs.keys())
        for key in keys_list:
            value = kwargs[key]
            for cls in Manager.class_list:
                if cls.__name__ == cls_name:
                    for item_obj in eval('cls.' + cls_objs_list_str):
                        if getattr(item_obj, key) == value:
                            return item_obj

            else:
                print('Nothing Found . . . !')

    def update(self):
        obj_info = input('Enter The Item\'s kez value:').split()
        kwargs = {obj_info[0]: obj_info[1]}
        item_obj = self.manager.search(self, **kwargs)
        print(item_obj.serializer())
        attr = input('Enter The attr you want to Update: ')
        new_value = input('Enter the new value: ')
        setattr(item_obj, attr, new_value)

    def check_load_flg(func):
        def inner(class_self, self):
            if not Manager.flag:
                func(class_self, self)

        return inner

    # @classmethod
    @check_load_flg
    def save_data(class_self, self):
        client = MongoClient()
        cls_collection = class_self.__name__ + 's'
        with client:
            db = client.Restaurant
            coll = eval('db.' + cls_collection)
            coll.insert_one(self.serializer())
        # with open(path, 'w') as f:
        #     f.write(json.dumps(data))

    @classmethod
    def load_data(cls, class_self):
        Manager.flag = True
        client = MongoClient()
        cls_collection = class_self.__name__ + 's'
        with client:
            db = client.Restaurant
            coll = eval('db.' + cls_collection)
            for every_obj in coll.find():
                eval('class_self(**every_obj)')

    @classmethod
    def show_menu(cls):
        for _class in cls.class_list:
            cls_name = _class.__name__
            cls_objs_list_str = cls_name.lower() + '_list'
            for item_obj in eval('_class.' + cls_objs_list_str):
                print(item_obj.serializer())


class ClassBase:
    manager = Manager

    # @abstractmethod
    # def introduce_class_name(self):
    #     pass
