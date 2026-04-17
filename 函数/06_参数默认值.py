def greet(name, /, age, *, gender, height,msg= '你好'):
    print(f"{msg}我叫{name}，今年{age}岁，{gender}性，身高{height}cm")
  

greet("知识", 19, gender="女", height=190,msg='hello')
