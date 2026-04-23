class Person:
    def __init__(self,name,age,idcard):
        self.name = name  # 公有属性
        self._age = age   # 受保护的属性，在当前类 子类 可以访问
        self.__idcard = idcard # 私有属性 只能在当前类访问

    # 注册处age属性getter方法，当访问Person实例age属性时，下面的age方法会被自动调用
    @property
    def age(self):
        return self._age

    # 注册处age属性setter方法，当修改Person实例age属性时，下面的age方法会被自动调用
    @age.setter
    def age(self,val):
        self._age = val

    @property
    def idcard(self):
        return self.__idcard[:6] + '********' + self.__idcard[-4:]
    @idcard.setter
    def idcard(self,value):
        print('card不能修改')

p1 = Person('zs',15,'15161142141')
print(p1.idcard)
p1.idcard = '2131241245'
