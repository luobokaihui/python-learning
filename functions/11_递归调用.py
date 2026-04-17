#  5 4 3 2 1
def test1(args):
    print(f'第{args}次，你好啊')
    if args > 1 :
        test1(args - 1)
# 1 2 3 4 5
def test2(args):
    if args > 1 :
        test2(args - 1)
    print(f'第{args}次，你好啊')
    
    

test1(5)
test2(5)