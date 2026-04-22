# list[起始索引:结束索引:步长]  步长为n 每次跳过 n - 1 取出元素

list1 = [10,20,30,40,50,60,70,80,90]
list2 = list1[1:5:1]
list3 = list1[2:8:3]
list4 = list1[::]

print(list2)
print(f'{list3}')
list4[2] = 100
print(list1)
print(list4)
print(list1 + list2)
tuple1 = (10,20,30,40,50,60)
tuple2 = tuple1[2:5:2]
print(tuple2)

str1 = 'hello word'
str2 = str1[2:7:4]
print(str2)
