# 定义一个Person类

class Person:
    # 当一个函数被定义在类中时，这个函数被称为:方法.

    # __init__ 初始化方法: 给当前正在创建的实例对象添加属性
    # __init__方法收到的参数: 当前正在创建的实例对象（self）、其他的自定义参数
    # 当去创建Person类的时候，Python会自动调用__init__犯法
    def __init__(self,name,age,gender):
        # 给实例添加属性(语法为 self.属性名 = 值)
        self.name = name
        self.age = age
        self.gender = gender

