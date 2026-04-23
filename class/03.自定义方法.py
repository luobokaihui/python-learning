class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法 给实例添加行为
    def speak(self,msg):
        print(f'我叫{self.name}，年龄{self.age}，性别{self.gender}，我要说{msg}')

# 创建实例对象
p1 = Person('章三',19,'女')

# 所有Person类得实例对象，都可以调用speak方法
p1.speak('这是p1所调用')
print(p1.__dict__)
