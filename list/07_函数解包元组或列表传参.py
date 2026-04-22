def demo(*args):
    print(f'这是demo函数，接收的参数是{args}')

ls1 = [100,200,300]
tuple1 = ('展示','实质','无奈')
demo(*ls1)
demo(*tuple1)


str1 = '这是我hello word这是我'

result = str1.strip('我这')
print(f'{result}')
