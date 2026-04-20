num = [10,20,30,40,50]
num.append(60)
num.insert(3,200)
num.extend(range(1,10))
result = num.pop(1)
num.remove(6)
del num[7]
print(num,result)
