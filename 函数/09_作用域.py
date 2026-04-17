# a = 100
# b = 200
# def test():
#     c = 300
#     a = 500
#     print(f'aaaa::{a}')
#     print(f'bbbb::{b}')
#     print(f'cccc::{c}')
# test()
# print(f'全局打印a::{a}')

a = 100
b = 200
def test():
    c = 300
    # 在函数修改全局变量 需要global 否则python会创建局部变量
    global a
    a = 500
    print(f'aaaa::{a}')
    print(f'bbbb::{b}')
    print(f'cccc::{c}')
test()
print(f'全局打印a::{a}')