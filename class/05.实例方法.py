class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法 给实例添加行为
    def speak(self,msg):
        print(f'我叫{self.name}，年龄{self.age}，性别{self.gender}，我要说{msg}')

    def run(self,distance):
        print(f'{self.name}跑了{distance}米')

p1 = Person('章三',15,'女')
p1.run(1000)
