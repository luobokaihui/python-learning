class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f'我叫{self.name}，年龄{self.age}，性别{self.gender}')

class Worker:
    def __init__(self,company):
        self.company = company

    def do_work(self):
        print(f'我在{self.company}做兼职')

class Students(Person,Worker):
    def __init__(self,name,age,gender,company,stu_id,grade):
        Person.__init__(self,name,age,gender)
        Worker.__init__(self,company)
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我在努力的学习，争取做{self.grade}年级的第一名')

s1 = Students('礼花',20,'女','超市','39415','初二')
s1.speak()
s1.do_work()
s1.study()
