def test1(*args):
    print(f"{args}")


test1("zs", "ls", 19, 2048)

def test2(*args , age,**kwargs):
    print(f'{args},{age},{kwargs}')

test2('zs',14,'asdf',age=15,height=140)