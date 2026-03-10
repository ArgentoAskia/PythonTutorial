"""
Python 类型说明总结：

## 1.
变量名 不需要声明类型：var = 2;
1. 第一个字符必须是字母表中字母或下划线_
2. 标识符的其他的部分由字母、数字和下划线组成
3. 标识符对大小写敏感
4. 不能是关键字

总结：既然Python是基于C来写的，那我们使用C的命名方式[蛇形命名法]很OK：hello_world

常量：大写字母表示：MAX_VALUE
1. 官方推荐的常量是约定，而非语法糖，开发者仍然能修改
2. 3.4+ 推荐使用枚举Enum替代

## 2.
基本数据类型：Number(complex)、String、Bool
复合数据类型：Tuple(元组)、List(列表)、Dictionary(字典)、Set(集合)

## 3.
使用type()查看具体的类型：
var = 2
type(var)

## 4.
作用域：LEGB原则
1. Local ==> 函数内部
2. Enclosing ==> 嵌套函数中的外层函数
3. Global ==> 模块级别
4. Built-in ==> Python内置
5. global 和 nonlocal关键字优先级最高

## 5.
输出使用print()

"""

# 定义变量
number = 2
is_number = True
float_number = 3.4
complex_number = 3 + 4j
print(f'{number},类型为：{type(number)}')
print(f'{is_number},类型为：{type(is_number)}')
print(f'{float_number},类型为：{type(float_number)}')
print(f'{complex_number},类型为：{type(complex_number)}')

name = "Ask"
print(f'{name},类型为：{type(name)}')


# 常量定义
MAX_VALUE = 2
print(MAX_VALUE)









