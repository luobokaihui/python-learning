s1 = {10,20,30,40,50}
s2 = {60,151,11}

# result = s1.difference(s2)
# s1.difference_update(s2)
# res2 = s1.union(s2)
# print(result)
# print(s1,s2)
# print(res2)

# issuperset 判断s1是否是s2的超集
res3 = s1.issuperset(s2)
print(res3)
# isdisjoint 判断s1和s2是否没有交集
res4 = s1.isdisjoint(s2)
print(res4)
