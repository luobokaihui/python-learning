def greet(name, age, gender, height):
    print(f"我叫{name}，今年{age}岁，{gender}性，身高{height}cm")

# 位置参数必须在关键字参数前
greet(age=21,gender='女',name='张三',height=240)
