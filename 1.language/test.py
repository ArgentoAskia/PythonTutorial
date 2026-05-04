import test_package as tst
from test_package import test as test2
from test_package.test import f1 as test2_f1
print('Hello')

__all__=['f1', '_f4']

x = 42

def f1():
    pass
    print('f1')


def f2():
    pass
    print('f2')


def f3():
    pass
    print('f3')


def _f4():
    pass
    print('_f4')

