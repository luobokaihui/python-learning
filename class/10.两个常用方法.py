class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):
        super().__init__(name,age,gender)
        self.stu_id = stu_id
        self.grade = grade

p1 = Person('章三',15,'女')
s1 = Student('礼花',16,'男','12315','五年级')
# 方法1:isinstance（instance,Class）判断某个对象是否为指定类或其子类的实例
print(isinstance(p1,Person))
print(isinstance(p1,Student))
print(isinstance(s1,Student))
print(isinstance(s1,Person))

# 方法2:issubclass（Class1,Class2）判断某个类是否是另一个类的子类
print(issubclass(Student,Person))
