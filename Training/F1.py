a=10
b=20
c=a+b
print(c)
def f1():
    print('inside f1 function')
    a=11
    b=12
    def f2():
        print('inside f2')
        b=33
        y=99
    f2()
f1()

def f3():
    print('inside f3')
    m=222
    n=333
f3()

import gc
print(gc.isenabled())