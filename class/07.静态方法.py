from datetime import datetime
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 静态方法
    # 使用 @staticmethod 装饰器装饰过的方法为静态方法，静态方法也是保存在类上的
    # 静态方法只是单纯定义在类中，只能收到自定义参数，不会接收self、cls参数
    # 由于静态方法没有接收self、cls参数，所以内部不会访问任何：类和实例相关的内容
    # 静态方法通常用于定于与类相关的工具方法
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - year
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '********' + idcard[-4:]

result = Person.mask_idcard('232324199912134814')
print(result)
