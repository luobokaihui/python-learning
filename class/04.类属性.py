
class Person:
    # max_age、plante 是类属性，并且类属性保存在类身上
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存:公共数据
    max_age = 120
    planet = '地球'

    def __init__(self,name,age,gender):
        # 给实例添加属性
        self.name = name
        self.gender = gender
        if 0 <= age < 120:
            self.age = age
        else:
            print(f'年龄超过最大限制{Person.max_age}')
            self.age = Person.max_age

p1 = Person('章三',0,'女')

print(p1.__dict__)

print(Person.max_age)
print(p1.max_age)
