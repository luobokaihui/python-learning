#  ' / ' 之前都使用位置参数 ' * ' 后面都使用关键字参数
def greet(name, /, age, *, gender, height):
    print(f"我叫{name}，今年{age}岁，{gender}性，身高{height}cm")


greet("知识", 19, gender="女", height=190)
