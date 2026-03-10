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
输入使用input()

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

print()
# 常量定义
MAX_VALUE = 2
print(MAX_VALUE)


# List 结构
## 1. 和数组很像可以使用下标访问, 支持负数下标，从0开始
## 2. 使用[]初始化，可以混合放入任何东西，甚至可以List嵌套List和其他结构, 不能越界访问和添加
## 3. 使用[上标:下标:步长]截断, 标可以是负数, 代表从末尾获取，截断不包括下标的位置，上标省略==>0[如果是倒叙步长则是最后一个元素]，下标省略==>列表的最后一个元素[这个最后的元素是相对的，如果是倒序步长，则会到第一个元素为止]，步长省略==>1
## 4. 使用+拼接两个List
## 总结：数组plus pro max版本，满足你对数组最终形态的一切幻想

## 初始化
print()
tiny_list = [123, 'runoob']
mix_list = [ 'abcd', 786 , 2.23, 'runoob', 70.2, True, 1 + 2j, [123, 456]]  # 定义一个列表

## 下标访问
print(mix_list[2])
print(mix_list[-2])
## 使用变量名可以输出全部元素,可以使用*2代表输出计次
print(mix_list)
print(mix_list * 2)

## 子列表
print(mix_list[1:3])        # 获取第二个到第四个元素【不包括第四个】
print(mix_list[:2])         # 从第三个
print(mix_list[::2])        # 获取偶数下标的元素
print(mix_list[-1:0:-1])    # 倒序输出除了第一个元素之外的所有元素1
print(mix_list[::-1])       # 倒叙输出所有元素
print(mix_list[2:4:-1])     # 如果规定错了顺序, 则会输出[]列表，比如要求从第3个元素开始截取
                            # 到第4个元素为止（包括）,但我们使用倒叙步长，则无法截取任何元素
print(mix_list[1::2])       # 获取奇数下标的元素
## 拼接
print(mix_list + tiny_list)
## 自拼接
print(tiny_list * 3)
print(mix_list * 2)
print()
# tuple(元组)
## 1.所有对List的规则同样适用于tuple
## 2.使用()初始化, 也可以使用tuple()初始化字符的方式来初始化
## 3.tuple是不可变对象，任何对tuple的操作都会导致产生一个新的tuple对象

mix_tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tiny_tuple = (123, 'runoob')
string_tuple = tuple('2345ABCDSESSADS')
print(string_tuple)

print(mix_tuple[2])
print(mix_tuple[::-1])
print(mix_tuple + tiny_tuple)       # 不建议这样做！
print(mix_tuple * 2)

## 何为不可变对象？
## 像List这样的相同内容的List实际上是两个对象
tiny_list_2 = [123, 'runoob']
print(id(tiny_list_2))
print(id(tiny_list))
print(tiny_list_2 == tiny_list)
## 而tuple这样的相同内容的tuple实际上是同一个对象，因为底层会对内容相同的tuple进行缓存
tiny_tuple_2 = (123, 'runoob')
print(id(tiny_tuple_2))
print(id(tiny_tuple))
print(tiny_tuple_2 == tiny_tuple)
## 对List可以进行修改
tiny_list_2[1] = '333'
print(tiny_list_2)
## 对tuple无法修改
# tiny_tuple_2[1] = '222'
# print(tiny_tuple_2)


## !!!由于使用()创建，可能会和运算的()撞上, 所以只有一个元素时要加上,!!!
tup1 = ()   # 能被识别成tuple
tup2 = (20) # 被识别成括号, 也就是说tup2是整数
tup3 = (20,)# tuple ==> (20)

print(f'tup1={tup1}, type is {type(tup1)}')
print(f'tup2={tup2}, type is {type(tup2)}')
print(f'tup3={tup3}, type is {type(tup3)}')

print()

# Set(集合)
## 1.一种无序、可变的数据类型，用于存储唯一的元素
## 2. 使用{}初始化, 也可以使用set()初始化
## 3. 由于和Dictionary类型重复了，所以初始化空Set不能使用 num_set = {}
## 4. 支持交并补差集操作
## 5. 仅支持嵌套tuple

mix_set = { 'abcd', 786 , 2.23, 'runoob', 70.2, True, 1 + 2j, tuple('123121')}
empty_set = set()
print(mix_set)
print(empty_set)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
## 交并补差
print(f"差集：输出a中有而b中没有的：{a - b}" )       # a和b的差集
print(f"差集：输出b中有的a中没有的：{b - a}")        # a和b的差集
print(f'并集：输出a和b的并集：{a | b}')       # a和b的并集
print(f'交集：输出a和b的交集：{a & b}')       # a和b的交集
print(f'补集：输出a和b中不同时存在的元素：{a ^ b}')       # a 和 b 中不同时存在的元素
print()

# Dictionary(字典)：即一个无序的 **键(key) : 值(value)** 的集合
## 1. 使用`{}`创建, 空字典使用{}
## 2. 使用[key]进行访问
## 3. keys()输出所有键, values()输出所有值, items()转为键值对数组

empty_dict = {}
tiny_dict = {'name': 'runoob','code':1, 'site': 'www.runoob.com', 'set': (123, 456, 789)}
print(tiny_dict)
print(tiny_dict.items())
print(tiny_dict.keys())
print(tiny_dict.values())
print(tiny_dict['name'])
print()


# 作用域
## LEGB local>enclosing>global>built-in
x = "global"          # 全局变量
def outer():
    x = "enclosing"   # 外层变量
    def inner():
        x = "local"   # 局部变量
        print(x)      # 输出: local
    inner()
    print(x)
outer()
print(x)
print()
## global 和 nonlocal
x = "global"          # 全局变量
def outer():
    c = "enclosing"   # 外层变量
    def inner():
        global x      # 使用global变量
        print(x)
        nonlocal c    # 使用外层的enclosing变量
        c = "nonlocal enclosing"
    inner()
    print(c)
outer()
print(x)






