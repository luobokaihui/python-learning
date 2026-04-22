t1 = (24,15,16,72)

print(type(t1))

l1 = list()
l2 = []
t2 = ('nihjao',)
print(type(t2))

def demo(*args):
    return sum(args)
result = demo(100,200,300)
print(f'{result}')

index = 0
while index < len(t1):
    print(f'{t1[index]}')
    index += 1

for item, index in enumerate(t1):
    print(item,index)
