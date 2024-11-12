from pprint import pprint
import inspect
from threading import Thread


class Class():

    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        attrib = []
        info_dict = {}

        info_dict['0 object '] = self.obj

        info_dict['1 type'] = type(self.obj)

        info_dict['2 class'] = inspect.isclass(self.obj)

        info_dict['3 attributes'] = dir(self.obj)

        info_dict['4 module'] = inspect.ismodule(self.obj)

        info_dict['5 function'] = inspect.isfunction(self.obj)

        info_dict['6 metod'] = inspect.ismethod(self.obj)


        return info_dict


object_1 = Class(Thread)
object_2 = Class(123)
object_3 = Class('Денис')
print('___________________________________')
pprint(object_1.introspection_info())
print('___________________________________')
pprint(object_2.introspection_info())
print('___________________________________')
pprint(object_3.introspection_info())
