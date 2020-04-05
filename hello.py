import calendar
import math
import sys
import time  # 引入time模块
import os
import re

from myModule import print_func
from package_runoob.runoob1 import runoob1

# 导入 Animal 类
from package_class.Animal import Animal
from package_class.Cat import Cat


print("你好，世界")
print('hello python')

# 1. Pyhton 标识符
# 单下划线开头，表示私有属性，需通过接口访问
# 双下划线表示类的私有成员
# 双下划线开头结尾镖师Python里特事故方法专用标识，如 __init__() 代表类的构造函数
# Python 可以同一行显示多条语句，方法是用 “；” 分割

# Python 格式 行和缩进
if True:
    print('True')
else:
    print('False')

# 多行语句 用斜杠（ \）将一行的语句分为多行显示

item_one = '1'
item_two = '2'
item_three = '3'
total = item_one + \
    item_two + \
    item_three
print(total)

'''
这里是多行注释
'''

# 等待用户输入
# input("按下 enter 键退出，其他任意键显示...\n")

# 同一行显示多条语句
x = 'runoob'
sys.stdout.write(x + '\n')

# 多个语句构成代码组
expression = True
expression2 = False
suite = '8848'
if expression:
    print(suite)
elif expression2:
    suite
    print(suite)
else:
    suite
    print(suite)

# 2. 变量类型

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print(counter)
print(miles)
print(name)

a, b, c = 1, 2, "john"
print(a, b, c)

# 实现从字符串中获取一段子字符串
s = '123456789'
splitS = s[1:5]
print(splitS)

# 更多字符串的操作 加号（+）是字符串连接运算符，星号（*）是重复操作
str = 'Hello World!'

print(str)           # 输出完整字符串
print(str[0])        # 输出字符串中的第一个字符
print(str[2:5])      # 输出字符串中第三个至第六个之间的字符串
print(str[2:])     # 输出从第三个字符开始的字符串
print(str * 2)       # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串

# Python 列表截取可以接收第三个参数，参数作用是截取的步长
str2 = 'Hello World!'
print(str2[1:4:2])

# 列表
tArr = [111, 222, 333]
print(tArr[0])  # 输出列表的第一个元素
print(tArr[1:3])  # 输出第二个至第三个元素
print(tArr[1:])  # 输出从第二个开始至列表末尾的所有元素
print(tArr[:1])  # 输出开始到第二哥元素
print(tArr[:])  # 输出完整列表
print(tArr * 2)  # 输出列表两次
print(tArr + [0, 0, 0])


# Python 元组
# 元组是另一个数据类型，类似于 List（列表）。
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
# 操作方法同列表类似


# Python 字典
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


# Python数据类型转换 https://www.runoob.com/python/python-variable-types.html
print(int(3.255))

# 3. Python 运算符

# Python算术运算符
#  + - * / %(取模 - 返回除法的余数) **(幂 - 返回x的y次幂) //(取整除 - 返回商的整数部分（向下取整）)

num1 = 10
num2 = 20
print(num2 ** num2)


# Python比较运算符
# ==	等于 - 比较对象是否相等
# !=	不等于 - 比较两个对象是否不相等
# >	大于 - 返回x是否大于y
# <	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。
# >=	大于等于	- 返回x是否大于等于y。
# <=	小于等于 -	返回x是否小于等于y。

a = 21
b = 10
if a > b:
    print('a > b')
else:
    print('a < b')

# Python赋值运算符
# =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
# =	加法赋值运算符	c += a 等效于 c = c + a
# =	减法赋值运算符	c -= a 等效于 c = c - a
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a

a *= b
print(a)

# Python位运算符
# 按位运算符是把数字看作二进制来进行计算的
# &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
# |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
# ^	按位异或运算符：当两对应的二进位相异时，结果为1
# ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
# <<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
# >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

w = a << 2
print(w)

# Python逻辑运算符
# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
# or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。

c = False
print(a and b)
print(c and b)

# Python成员运算符
# in	如果在指定的序列中找到值返回 True，否则返回 False。
# not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

aa = '123456789'
print('3' in aa)

# Python身份运算符
# 身份运算符用于比较两个对象的存储单元
# is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

bb = '123456789'
print(aa is bb)

# Python运算符优先级

# 4. Python 条件语句 if XXX: else: XXX

# 5. Python 循环语句

# 5.1 Python While 循环语句

aw = 10
while aw < 20:
    print(aw)
    aw += 1

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立

# 循环使用 else 语句
# 在 python 中，while … else 在循环条件为 false 时执行 else 语句块：

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

# 5.2 Python for 循环语句

for letter in 'Python':     # 第一个实例
    print('当前字母 :', letter)

# 通过序列索引迭代

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print(index)
    print('当前水果 :', fruits[index])

# 循环使用 else 语句

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:      # 确定第一个因子
            j = num/i          # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print(num, '是一个质数')


# 6. Python随机数函数

# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# random()	随机生成下一个实数，它在[0,1)范围内。
# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	将序列的所有元素随机排序
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

# 7. Python三角函数
# acos(x)	返回x的反余弦弧度值。
# asin(x)	返回x的反正弦弧度值。
# atan(x)	返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	返回的x弧度的正弦值。
# tan(x)	返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	将角度转换为弧度

# 8. Python数学常量 pi e

#  9. Python 字符串格式化

print("My name is %s and weight is %d kg!" % ('Zara', 21))


# 10. 列表
# 更新列表

list = []  # 空列表
list.append('Google')  # 使用 append() 添加元素
list.append('Baidu')
print(list)

# 删除列表元素

del list[1]
print(list)

# Python列表脚本操作符
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3	迭代

# Python列表截取

L = ['Google', 'Runoob', 'Taobao']

# L[-2]	'Runoob'	读取列表中倒数第二个元素
# L[1:]	['Runoob', 'Taobao']	从第二个元素开始截取列表
print(L[2])  # 读取列表中第三个元素

# Python列表函数&方法
# cmp(list1, list2) 比较两个列表的元素
# len(list) 个数
# max(list) 最大值
# min(list) 最小值
# list(seq) 将元组转换为列表

# Python包含以下方法:
# list.append(obj)
# list.count(obj) 统计某个元素在列表中出现的次数
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj) 将对象插入列表
# list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj) 移除列表中某个值的第一个匹配项
# list.reverse() 反向列表中元素
# list.sort(cmp=None, key=None, reverse=False) 对原列表进行排序

# 10. 字典

dict = {'a': 1, 'b': 2, 'c': '3'}
print(dict['b'])

dict['c'] = '131231'
print(dict)

del dict['c']
print(dict)

# 字典内置函数&方法
# cmp(dict1, dict2) 比较两个字典元素
# len(dict) 计算字典元素个数，即键的总数。
# str(dict) 输出字典可打印的字符串表示。
# type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。
# dict.clear() 删除字典内所有元素
# dict.copy() 返回一个字典的浅复制
# dict.fromkeys(seq[, val]) 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
# dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
# dict.has_key(key) 如果键在字典dict里返回true，否则返回false
# dict.items() 以列表返回可遍历的(键, 值) 元组数组
# dict.keys() 以列表返回一个字典所有的键
# dict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# dict.update(dict2) 把字典dict2的键/值对更新到dict里
# dict.values() 以列表返回字典中的所有值
# pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# popitem() 返回并删除字典中的最后一对键和值。

# 11. 时间


ticks = time.time()
print("当前时间戳为:", ticks)

# localtime = time.localtime(time.time())
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

cal = calendar.month(2016, 1)
print(cal)

# 12. 定义python 函数


def getDate(date='2020'):
    return date


print(getDate('2020 4-5'))

# 匿名函数


def sum(arg1, arg2): return arg1 + arg2


print(sum(10, 20))

# 13. 模块化
# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

print_func('123')

# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

print(dir(math))


# 模块化包

runoob1()

# 14. IO

# input

str = input("请输入...")
print("您输入的是:", str)



try:
    fo = open('./learnPython/iofile/iotest.text', "w")  # 打开该文件 只写入
except expression as identifier:
    print('文件写入出错!')
else:
    fo.write('5201314~')  # 写入
    fo.close()

# 15. 定义类

animal = Animal('小猫', '橘黄', '喵呜~')
print(animal.getSpeak()) # 调用方法
cat = Cat('小黄')
print(cat.getName())

# 16. 正则表达式

#  案例,匹配身份证信息
s = '138723198012123718'
result = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(result.groupdict())