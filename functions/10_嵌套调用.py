def test1():
    print(f'进入test1函数')
    test2()
    print('退出test1函数')
    
def test2():
    print(f'进入test2函数')
    test3()
    print('退出test2函数')
    
def test3():
    print(f'进入test3函数')
    print('******正在执行*******')
    print('退出test3函数')

test1()