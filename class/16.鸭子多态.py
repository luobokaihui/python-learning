# 核心理念：如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子
# 鸭子类型是一种编程风格，它不检查对象类型，只关注对象能否做“某件事”（是否有对应的方法）

class Dog:
    def __init__(self):
        pass

    def speak(self):
        print('汪汪汪')

class Cat:
    def __init__(self):
        pass

    def speak(self):
        print('喵喵喵')

class Fish:
    def __init__(self):
        pass

    def speak(self):
        print('咕噜噜')

def make_sound(animal):
    animal.speak()

d1 = Dog()
c1 = Cat()
f1 = Fish()

make_sound(d1)
make_sound(c1)
make_sound(f1)
