# 【抽象类】是一种不能直接实例化的类,它通常作为“规范”,让子类去继承,并实现其中定义的“抽象方法”.
from abc import ABC,abstractmethod

# 类一旦继承ABC类 就是抽象类
class MustRun(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def run(self):
        pass

class Person(MustRun):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑')

p1 = Person('章三',20,'男')
p1.run()
