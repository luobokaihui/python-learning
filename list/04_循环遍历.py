list = [14,15,12,16,13,11,10]

index = 0
while index < len(list):
    print(list[index])
    index += 1

print(f'***************\n')
for item in list:
    print(item)
print(f'***************\n')
for item in range(len(list)):
    print(list[item])
print(f'***************\n')
for item, index in enumerate(list):
    print(f'{item},{index}')

