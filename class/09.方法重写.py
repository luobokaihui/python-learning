class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f'我叫{self.name}，年龄{self.age}，性别{self.gender}，我要说{msg}')

class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):
        super().__init__(name,age,gender)
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我叫{self.name}，几年{self.age}岁，学号是{self.stu_id},争取做到{self.grade}第一')

    def speak(self,msg):
        super().speak(msg)
        print(f'这是Student的speak方法')

s1 = Student('礼花',14,'女','2013-145','六年级')
s1.speak('学习')
