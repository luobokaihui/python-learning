class Person:
    def __init__(self,name,age,idcard):
        self.name = name  # 公有属性
        self._age = age   # 受保护的属性，在当前类 子类 可以访问
        self.__idcard = idcard # 私有属性 只能在当前类访问

    def speak(self):
        print(f'我叫{self.name}，年龄{self._age}，身份证{self.__idcard}')

p1 = Person('装饰',26,'2351616')
p1.speak()
print(p1.name,p1._age)
