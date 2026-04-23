class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

# 创建Person类的实例对象
p1 = Person('章三',15,'男')
p2 = Person('李四',19,'女')

# 通过点语法可以访问或修改实例身上的属性
print(p1.name,p1.age,p1.gender)
print(p2.name,p2.age,p2.gender)
p1.name = '王五'
print(p1.name)

# 通过 实例.__dict__ 可以查看实例身上的所有属性

print(p1.__dict__)

# 实力创建完成后 可以通过 实例.属性名 = 值 给实例追加属性

p1.address = '长沙' # type: ignore
print(p1.__dict__)

# 通过type函数 可以查看某个实例对象是由哪个类创建出来的
print(type(p1))
print(type(p2))
