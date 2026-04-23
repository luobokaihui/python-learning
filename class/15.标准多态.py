# 多态的概念: 同一个方法名 在不同的对象上调用，能呈现出不同的行为
# Python中支持:标准多态  鸭子多态

class Animal:
    def __init__(self):
        pass

    def speak(self):
        print('动物发出叫声')

class Dog(Animal):
    def __init__(self):
        pass

    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def __init__(self):
        pass

    def speak(self):
        print('喵喵喵')

def make_sound(animal:Animal):
    animal.speak()

a1 = Animal()
a2 = Dog()
a3 = Cat()
make_sound(a1)
make_sound(a2)
make_sound(a3)
