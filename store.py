import json

from lib import FILE_PATH
from json import *
class Store:

    @classmethod
    def save_to_file(cls,path,data):
        with open(path,'w') as f:
            f.write(json.dumps(data))


    @classmethod
    def load_from_file(cls,path):
        with open(path,'r') as f:
            f.readlines(json.load())

