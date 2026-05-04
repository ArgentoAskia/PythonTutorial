## 函数定义：
## 1、使用def关键字
## 2、函数名
## 3、参数不需要标明类型
def max_fun(a, b):
    if a > b:
        return a
    else:
        return b


## 4.函数调用
## 5.函数传递(对象引用传递)
## 不可变对象（值传递）VS 可变对象（引用传递）
print(max_fun(2, 3))

## 不可变对象
def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象
a = 1
print(id(a))
change(a)


# 可变实例
def change_me(my_list):
    """修改传入的列表"""
    my_list.append([1, 2, 3, 4])
    print("函数内取值: ", my_list)
    return
# 调用change_me函数
mylist = [10, 20, 30]
change_me(mylist)
print("函数外取值: ", mylist)

## 6.参数传递：
### 必须参数, 关键字参数, 可选参数[默认参数], 不定长参数

## 必须参数
### 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# 可写函数说明
def print_me_must(str):
    """打印任何传入的字符串"""
    print(str)
    return
# 调用 printme 函数，不加参数会报错
print_me_must('123')

## 关键字参数
### 使用参数名作为关键字。
### 指定参数是哪一个，这样可以让参数忽略顺序传递
def print_me_keyword(str, number):
    """打印任何传入的字符串"""
    print(str, number)
    return


# 调用printme函数
print_me_keyword(number=1, str="菜鸟教程")

## 默认参数
### 调用函数时，如果没有传递参数，则会使用默认参数
def print_info(name, age=35):
    """打印任何传入的字符串"""
    print("名字: ", name)
    print("年龄: ", age)
    return
# 调用printinfo函数
print_info(age=50, name="runoob")
print("------------------------")
print_info(name="runoob")


## 不定长参数
### 1.不定长参数以*开头，并且必须放在最后，每种类型只能有一个
### 2.有两种：*args ==> 被解析成元组
###        **kwargs==> 被解析成字典
### 3. 最多最多可以有 1 个 *args 和 1 个 **kwargs

### 参数优先级：普通位置参数 → 默认参数 → *args → 命名关键字参数 → **kwargs

def demo(a, b=10, *args, c, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}")
    print(f"kwargs={kwargs}")
# 调用
demo(1, 2, 3, 4, c=5, d=6, e=7)

## 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
def f(a,b,*,c):
    return a+b+c
print(f(1, 2, c=3))

## Lambda表达式，匿名函数
## lambda [arg1 [,arg2,.....argn]]:expression
## 只能使用表达式而不是代码块


"""
一个演示多种函数特性的模块
"""

from typing import List, Optional
from functools import wraps, partial
import time

# 1. 基本函数与类型注解
def greet(name: str, greeting: str = "Hello") -> str:
    """返回问候语"""
    return f"{greeting}, {name}!"

# 2. 可变参数
def average(*args: float) -> Optional[float]:
    """计算平均值，无参数返回 None"""
    if not args:
        return None
    return sum(args) / len(args)

# 3. 装饰器示例：计时
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

# 4. 生成器
def fibonacci(n: int):
    """生成斐波那契数列，最多 n 项"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 5. 闭包
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# 6. 使用装饰器
@timer
def compute_fibonacci_sum(n: int) -> int:
    """计算前 n 个斐波那契数的和"""
    return sum(fibonacci(n))

if __name__ == "__main__":
    print(greet("World"))
    print(average(1, 2, 3, 4))          # 2.5
    print(average())                    # None

    counter = make_counter()
    print(counter())                    # 1
    print(counter())                    # 2

    total = compute_fibonacci_sum(100)
    print(f"Sum of first 100 Fibonacci numbers: {total}")

    # 偏函数
    greet_en = partial(greet, greeting="Hi")
    print(greet_en("Alice"))

