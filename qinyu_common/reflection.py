import importlib


def object_from_classpath(classpath, **kwargs):
     classpath = str_to_type(classpath)
     return classpath()

def str_to_type(classpath):
    module_name, class_name = classpath.rsplit('.', 1)
    #根据给定的模块名和类名，获取该模块中的对应类
    cls = getattr(importlib.import_module(module_name), class_name)
    return cls
