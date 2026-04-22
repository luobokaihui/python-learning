s1 = {1,1,1,True,0,False,'12312','124'}
s2 = {'zs','s','zs','呜呜呜呜'}

print(f'{type(s1)} {s1}')
print(f'{type(s2)} {s2}')

# 不可变集合
s3 = frozenset(s1)
s4 = frozenset(s2)

print(f'{type(s3)} {s3}')
print(f'{type(s4)} {s4}')
