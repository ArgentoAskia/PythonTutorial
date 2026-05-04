# 算数运算符
## +  -  *  /  %   **   //
## 加 减 乘 除 取模  幂  整除（小方向）

a = 21
b = 10
c = 0

c = a + b
print ("1 - c 的值为：", c)
c = a - b
print ("2 - c 的值为：", c)
c = a * b
print ("3 - c 的值为：", c)
c = a / b
print ("4 - c 的值为：", c)
c = a % b
print ("5 - c 的值为：", c)
c = a ** b
print ("6 - c 的值为：", c)
c = a // b
print ("7 - c 的值为：", c)
print()

# 比较运算符
## == 比较是否相等
## != 比较是否不等于
## > 大于
## < 小于
## >= 大于等于
## <= 小于等于
a = 21
b = 10
c = 0

if (a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if (a < b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if (a > b):
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if (b >= a):
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")



## 赋值运算符
## = 赋值
## += 加法赋值
## -= 减法赋值
## *= 乘法赋值
## /= 除法赋值
## %= 取模赋值
## **= 幂运算赋值
## //= 取整运算赋值
## := Py 3.8 海象运算符, 这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值。
# 1. 基本赋值与引用问题
print("=== 基本赋值与引用 ===")
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]

# 2. 复合赋值
print("\n=== 复合赋值 ===")
num = 10
num += 5
print(num)  # 15
num //= 2
print(num)  # 7

lst = [1, 2]
lst += [3]          # 原地修改
print(lst)          # [1, 2, 3]

# 3. 海象运算符
print("\n=== 海象运算符 ===")
import re
text = "The number is 42"
if (match := re.search(r'\d+', text)):
    print(f"Found number: {match.group()}")  # Found number: 42

# 4. 链式赋值与可变对象问题
print("\n=== 链式赋值 ===")
x = y = []
x.append(5)
print(y)  # [5]  指向同一对象

# 5. 解包赋值
print("\n=== 解包赋值 ===")
first, second, *others = range(5)
print(first, second, others)  # 0 1 [2, 3, 4]

# 6. 深拷贝 vs 赋值
print("\n=== 深拷贝 ===")
import copy
orig = [1, [2, 3]]
cop = orig   # 引用
cop[1].append(4)
print(orig)  # [1, [2, 3, 4]]
deep = copy.deepcopy(orig)
deep[1].append(5)
print(orig)  # 不变 [1, [2, 3, 4]]


## 逻辑运算符完整示例
"""
逻辑运算符完整示例
"""

def demo_short_circuit():
    print("\n=== 短路求值 ===")
    def f():
        print("f 被调用了")
        return True
    False and f()   # f 不打印
    True or f()     # f 不打印
    True and f()    # f 打印

def demo_return_value():
    print("\n=== 返回值（非布尔） ===")
    print(3 and 5)      # 5
    print(0 and 99)     # 0
    print([] or [1,2])  # [1,2]
    print("" or "default")  # "default"

def demo_falsy_values():
    print("\n=== 假值列表 ===")
    falsy = [False, None, 0, 0.0, 0j, "", [], (), {}, set(), range(0)]
    for val in falsy:
        if not val:
            print(f"{repr(val):12} -> 假")
    # 非假值示例
    truthy = [True, 1, -1, "hello", [0], (None,), {0:0}]
    for val in truthy:
        if val:
            print(f"{repr(val):12} -> 真")

def demo_common_pitfalls():
    print("\n=== 常见陷阱 ===")
    # 陷阱1：混淆 & 和 and
    a = 3  # 二进制 011
    b = 4  # 二进制 100
    print(f"a & b = {a & b} (位与)")  # 0
    print(f"a and b = {a and b} (逻辑与)")  # 4

    # 陷阱2：短路副作用
    x = 0
    def change_x():
        global x
        x = 100
        return True
    print("执行前 x =", x)
    result = False and change_x()
    print("执行后 x =", x)  # x 未被修改

    # 陷阱3：优先级
    val = True
    if val or False and False:  # 实际为 val or (False and False) -> True
        print("条件为真")

def demo_practical_usage():
    print("\n=== 实用技巧 ===")
    # 1. 默认值赋予
    user_input = ""
    name = user_input or "Guest"
    print(f"欢迎, {name}")

    # 2. 链式条件简化
    age = 25
    if 18 <= age <= 60:   # 等价于 age >= 18 and age <= 60
        print("工作年龄")

    # 3. 安全的属性访问（结合短路）
    config = None
    value = config and config.get("key")   # 不会抛出 AttributeError
    print(value)  # None

if __name__ == "__main__":
    demo_short_circuit()
    demo_return_value()
    demo_falsy_values()
    demo_common_pitfalls()
    demo_practical_usage()

## 位运算符

"""
Python 位运算符完整示例
"""

def bin_print(name, value):
    """辅助函数，打印十进制和二进制"""
    print(f"{name} = {value} = {bin(value)}")

def demo_basic():
    print("=== 基本位运算 ===")
    a = 0b1010   # 10
    b = 0b1100   # 12
    bin_print("a", a)
    bin_print("b", b)
    print(f"a & b = {a & b} ({bin(a & b)})")
    print(f"a | b = {a | b} ({bin(a | b)})")
    print(f"a ^ b = {a ^ b} ({bin(a ^ b)})")
    print(f"~a = {~a} ({bin(~a)})")
    print(f"a << 1 = {a << 1} ({bin(a << 1)})")
    print(f"a >> 1 = {a >> 1} ({bin(a >> 1)})")

def demo_negative():
    print("\n=== 负数位运算 ===")
    x = -10
    bin_print("x", x)
    print(f"~x = {~x}")          # 9
    print(f"x >> 1 = {x >> 1}")  # -5
    print(f"x << 1 = {x << 1}")  # -20

def demo_mask():
    print("\n=== 模拟固定宽度取反 ===")
    val = 0b0101  # 5
    mask = 0b1111  # 4位宽
    print(f"~{val} & 0b1111 = {(~val) & mask} ({bin((~val) & mask)})")

def demo_shift():
    print("\n=== 移位注意事项 ===")
    print(f"1 << 1000 太大不列出，长度 = {(1 << 1000).bit_length()}")  # 1001 位
    print(f"5 >> 200 = {5 >> 200}")  # 0
    print(f"-5 >> 1 = {-5 >> 1}")    # -3 (因为 -5 // 2 = -3)
    print(f"-5 // 2 = {-5 // 2}")    # 验证 -3

def demo_practical():
    print("\n=== 实用技巧 ===")
    # 奇偶
    for i in range(3):
        print(f"{i} 是 {'奇数' if i & 1 else '偶数'}")
    # 权限
    READ = 0b001
    WRITE = 0b010
    EXEC = 0b100
    perm = READ | WRITE
    print(f"权限掩码: {perm} ({bin(perm)})")
    print(f"可读: {bool(perm & READ)}")
    print(f"可执行: {bool(perm & EXEC)}")
    # 最低位
    x = 0b1101000
    lowbit = x & -x
    print(f"{x} 的最低为1的位: {lowbit} (位置 {lowbit.bit_length() - 1})")
    # Python 3.8+ popcount
    print(f"{x} 的二进制中 1 的个数: {x.bit_count()}")

def demo_trap():
    print("\n=== 常见陷阱 ===")
    # 优先级
    a = 2
    b = 3
    c = a | b + 1
    print(f"2 | 3 + 1 = {c} (实际为 2 | 4 = 6)")
    # 混淆 & 和 and
    print(f"2 & 3 = {2 & 3}")
    print(f"2 and 3 = {2 and 3}")
    # 负数的无限精度取反
    print(f"~0 = {~0} (而不是 -1 吗？~0 = -1 正确)")
    print(f"~1 = {~1} (-2)")

if __name__ == "__main__":
    demo_basic()
    demo_negative()
    demo_mask()
    demo_shift()
    demo_practical()
    demo_trap()


"""
成员运算符完整示例
"""

def demo_basic():
    print("=== 基本用法 ===")
    # 列表
    lst = [1, 2, 3]
    print(f"2 in lst: {2 in lst}")
    print(f"4 not in lst: {4 not in lst}")
    # 字符串
    s = "hello"
    print(f"'ell' in 'hello': {'ell' in s}")
    # 字典
    d = {'a': 1, 'b': 2}
    print(f"'a' in d: {'a' in d}")
    print(f"1 in d: {1 in d}")
    print(f"1 in d.values(): {1 in d.values()}")
    # 集合
    st = {1, 2, 3}
    print(f"2 in st: {2 in st}")

def demo_performance():
    print("\n=== 性能对比 ===")
    import timeit
    n = 10000
    lst = list(range(n))
    st = set(lst)
    # 查找最后一个元素
    t1 = timeit.timeit(f'{n-1} in lst', globals=globals(), number=1000)
    t2 = timeit.timeit(f'{n-1} in st', globals=globals(), number=1000)
    print(f"List in: {t1:.5f}s")
    print(f"Set  in: {t2:.5f}s")

def demo_custom_class():
    print("\n=== 自定义类 ===")
    class EvenNumbers:
        def __contains__(self, item):
            return isinstance(item, int) and item % 2 == 0
    evens = EvenNumbers()
    print(f"2 in evens: {2 in evens}")
    print(f"3 in evens: {3 in evens}")

def demo_pitfalls():
    print("\n=== 常见陷阱 ===")
    # 字符串子串陷阱
    print("'he' in 'hello' ->", 'he' in 'hello')
    # 字典键陷阱
    d = {1: 'one', 2: 'two'}
    print("1 in d ->", 1 in d)
    print("'one' in d ->", 'one' in d)
    # 浮点数精度
    print("0.1+0.2 in [0.3] ->", 0.1+0.2 in [0.3])
    # generator 耗尽
    g = (x for x in range(3))
    print(f"2 in g: {2 in g}")
    print(f"1 in g: {1 in g} (因为生成器已结束)")

def demo_range():
    print("\n=== range 的高效 in ===")
    r = range(10**9)
    print(f"500_000_000 in r: {500_000_000 in r}")   # 很快
    # 但浮点数不行
    print(f"500_000_000.0 in r: {500_000_000.0 in r}")  # False

def demo_advanced():
    print("\n=== 进阶技巧 ===")
    # 简化条件
    x = 2
    if x in (1, 2, 3):
        print("x 是 1,2,3 之一")
    # 黑名单
    blocked = {'spam', 'bad'}
    word = 'hello'
    if word not in blocked:
        print("允许通过")
    # 路径部件检查
    from pathlib import Path
    p = Path('/usr/local/bin')
    print(f"'local' in p.parts: {'local' in p.parts}")

if __name__ == "__main__":
    demo_basic()
    demo_performance()
    demo_custom_class()
    demo_pitfalls()
    demo_range()
    demo_advanced()



