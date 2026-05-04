## 数学函数

print("================= 内置函数大全演示 =================")
print("================= 作者：Askia =================")
print()
print("================= 数学函数开始 =================")
## 1. abs(x) ==> 返回绝对值
n = abs(-5)
print(f"-5的绝对值是{n}")

## 2. divmod(a, b) ==> 返回商和余数的元组 (a//b, a%b)
ret = divmod(10, 3)
print(f"10除以3的返回值是{ret[0]}, 余数是{ret[1]}")

## 3. pow(x, y[, z]) ==> 返回x**y，若提供z, 则返回(x**y) % z。
ret = pow(2, 10)
print(f"2的10次方等于{ret}")
ret = pow(2, 10, 1000)
print(f"2的10次方和1000取余数等于{ret}")

## 4. round(x[, n]) ==> 四舍五入，`n` 为小数位数。
ret = round(3.14159, 2)
print(f"3.14159四舍五入保留两位小数 = {ret}")


## 5. `sum(iterable, start=0) ==> 求和，从 `start` 开始累加。
ret = sum([1,2,3,4,5,6,7,8,9,10])
print(f"1+2+...+10={ret}")
ret = sum([1,2,3,4,5,6,7,8,9,10], 4)
print(f"5+...+10={ret}")

## 6. max(a,b,c,d,e...) ==> 求最大值
ret = max(1, 5, 3)
print(f"1, 5, 3中的最大值是 = {ret}")

## 7. min(a,b,c,d,e...) ==> 求最小值
ret = min(1, 5, 3)
print(f"1, 5, 3中的最小值是 = {ret}")
print("================= 数学函数结束 =================")
print()

print("================= 内置函数开始 =================")

## 1. 类型构造器函数
## 1.1 int(x[, base=10]) ==> 将数字或字符串转为整数。base表示参数x是什么进制的。默认10
ret = int('101', 2)
print(f"101的2进制字符串 = {ret}")
## 1.2 float(x) ==> 将数字或字符串转为浮点数。(实际上并不是函数而是构造方法)
ret = float('3.14')
print(f"'3.14'字符串转float = {ret}")

ret = complex(2, 3)
print(f"复数 = {ret}")

ret = str(123)
print(f"整数123转字符串 = {ret}")

ret = bytes('hello', 'utf-8')
print(f"('hello', 'utf-8')转不可变bytes数组 = {ret}")

ret = bytearray('hello', 'utf-8')
print(f"('hello', 'utf-8')转可变bytearray = {ret}")

ret = list('abc')
print(f"转list('abc') = {ret}")

ret = tuple([1,2])
print(f"转tuple([1,2]) = {ret}")

ret = dict(a=1, b=2)
print(f"转dict(a=1, b=2) = {ret}")

ret = set('123')
print(f"转set('123') = {ret}")

ret = frozenset([1,2,3])
print(f"转frozenset([1,2,3]) = {ret}")

ret = bool([])
print(f"转bool([]) = {ret}")

## 2. chr(i) ==> 将整数（0-1114111）转为 Unicode 字符。
ret = chr(65)
print(f"65的ASCII码值：chr(65) = {ret}")

## 3. ord(c) ==> 将字符转为 Unicode 码点。
ret = ord('A')
print(f"'A'的ASCII整数：ord('A') = {ret}")

## 4. hex(x) ==> 转16进制字符串
ret = hex(255)
print(f"'255'的16进制字符串：hex(255) = {ret}")

## 5. oct(x) ==> 转8进制字符串
ret = oct(255)
print(f"'255'的8进制字符串：oct(255) = {ret}")

## 6. bin(x) ==> 转二进制字符串
ret = bin(255)
print(f"'255'的二进制字符串：bin(255) = {ret}")
print("================= 内置函数结束 =================")











