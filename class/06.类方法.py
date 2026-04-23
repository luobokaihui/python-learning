from datetime import datetime
class Person:
    max_age = 120
    planet = '地球'
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # speak、run方法都是实例方法
    def speak(self,msg):
        print(f'我叫{self.name}，年龄{self.age}，性别{self.gender}，我要说{msg}')

    def run(self,distance):
        print(f'{self.name}跑了{distance}米')

    # 类方法使用@classmethod装饰器
    # 类方法收到的参数： 当前类本身（cls）、自定义参数
    # 因为收到了cls参数所以类方法中可以访问类属性
    # 类方法通常用于实现：与类相关的逻辑，例如：参数类相关的信息、一些工厂方法
    @classmethod
    def change_planet(cls,value):
        cls.change_planet = value

    @classmethod
    def create(cls,info_str):
        name, year ,gender = info_str.split('-')
        print(name, year ,gender)
        current_year = datetime.now().year
        age = current_year - int(year)
        # 创建并返回一个Person类的实例对象
        return cls(name,age,gender)

p2 = Person.create('梨花-1987-女')

print(p2.__dict__)
