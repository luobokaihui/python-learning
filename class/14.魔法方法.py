# 以 __xxx__ 命名的特殊方法 (双下划线开头 双下划线结尾)
# 不需要手动调用，在某种特殊情况下 Python会自动调用
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 当执行print（Person的实例对象） 或 str（Person的实例对象）时候调用
    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender}'

    # 当执行len（Person的实例对象)时候调用
    def __len__(self):
        return len(self.__dict__)

    # 当执行 Person实例对象 < other实例对象 时候调用
    def __lt__(self, other):
        return self.age < other.age

    # 当执行 Person实例对象 > other实例对象 时候调用
    def __gt__(self, other):
        return self.age > other.age

    # 当执行 Person实例对象 == other实例对象 时候调用
    def __eq__(self,other):
        return self.__dict__ == other.__dict__

    # 当访问Person实例对象身上不存在的属性时调用
    def __getattr__(self, name):
        return f'你访问的{name}属性不存在'


p1 = Person('章三',26,'2351616')
p2 = Person('章三',26,'2351616')
print(p1)
print(len(p1))
print(p2 < p1)
print(p2 > p1)
print(p1 == p2)
print(p1.address)
