# TODO-1: Add Supervisor class Here
# TODO-1: Add .sample() classmethod for Supervisor which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)


class Supervisor:


    def __init__(self,username,password,number):
        self.username = username
        self.password = password
        self.phone = number


