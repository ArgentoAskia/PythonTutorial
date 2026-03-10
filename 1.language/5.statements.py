"""
语句：
- if、match...case...
- while、for、for...in...
- continue、break
- pass
"""
import random

## if演示
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")


num=int(input("输入一个分数："))
if 90 <= num <= 100:
    print("成绩优秀")
elif 70 <= num < 90:
    print("成绩良好")
elif 60 <= num < 70:
    print("成绩合格")
else:
    print("成绩不合格")


# match...case...
match 404:
    case 200 | 201 | 203:
        print("OK")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:     # 相当于default
        print("Something's wrong with the internet")


# for 计次循环，需要配合range()
for num in range(10,20):  # 迭代 10 到 20 (不包含) 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)


# for...in...循环
for letter in 'Python':  # 第一个实例
    print("当前字母: %s" % letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果: %s' % fruit)


# pass只作为占位符出现，实际上不执行任何东西，为了解决缩进导致的空函数定义问题
# 建议在所有doc后面跟pass
def func():
    """
    这个是文档
    :return:
    """
    pass
    print("hello world")
func()


# 该实例演示了数字猜谜游戏

number = random.randint(1, 100)
guess = -1
print("数字猜谜游戏!(1 - 100以内)")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")