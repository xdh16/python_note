#!/usr/bin/python
# -*- coding: UTF-8 -*-

print ("你好，世界")
#一行显示多条语句，方法是用分号 ; 分开
print ("hello"); print ("world")

#没有严格缩进，在执行时会报错
if True:
    print ("true")
    print ("Answer")
else:
    print ("flase")
    print ("NoAnswer")
print("False")

     
#python引号
word = 'word'
sentence = "这是一个句子"
paragraph = "这是一个段落"     

#单行注释
 
'''
这是多行注释，使用单引号
这是多行注释，使用单引号
这是多行注释，使用单引号
'''

x="a"
y="b"

#换行输出
print (x)
print (y)
#不换行输出
print (x,y)


#多语句判断

if True:
    print ("expressiona")
elif False:
    print ("expressionb")
else:
    print ("expression other")
    
    
#变量类型    
counter = 100    #整型
miles = 1000.0   #浮点型
name = "john"    #字符串

print (counter)
print (miles)
print (name)

#多个变量赋值
a=b=c=1
q,w,e = 1,2,"join"

print (a,b,c)
print (q,w,e)

var1 = 1
var2 = 10
del var1

str = 'Hello World!'
 
print (str)           # 输出完整字符串
print (str[0])        # 输出字符串中的第一个字符
print (str[2:5])      # 输出字符串中第三个至第六个之间的字符串
print (str[2:])       # 输出从第三个字符开始的字符串
print (str * 2)       # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串

#列表
list = ['android', 123, 1.23, 'hi']
tinylist = ['hi']

print (list)             # 输出完整列表
print (list[0])          # 输出列表的第一个元素
print (list[1:3])          # 输出第二个至第三个元素 
print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
print (list * 2)       # 输出列表两次
print (list + tinylist)    # 打印组合的列表

#元组
tuple = ('ros', 756, 2.23, 'join', 70.2)
tinytuple = (123, 'john')
 
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3])          # 输出第二个至第四个（不包含）的元素 
print (tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2)       # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组

#列表和元组的注意事项
list1 = ['android', 123, 1.23, 'hi']
tuple1 = ('ros', 756, 2.23, 'join', 70.2)

list1[2] = 1000  #列表能修改值
#tuple1[2] = 1000 #元组不能修改值, 修改会报错

#条件语句
data = 10
if (data >0 and data <5) or (data >=10 and data <20):
    print ("Is True")
else:
    print (data)
    print ("Is False")
    
#循环语句
for letter in 'python':
    print ('当前字母:', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print ("当前水果:", fruit)

print ("good bye")

#通过序号索引迭代
food = ['banana', 'apple', 'mango']
for index in range(len(food)):
    print ('当前水果: ', food[index])
print ("good bye")

#嵌套for循环语句
for num in range(10,20):
    for i in range(2,num):
        if i%2 == 0:
            print (i)
        else:
            break
    
#函数

#函数说明
def printinfo(name, age=35):
    print ("Name: ", name)
    print ("Age:", age)
    return
    
#调用函数    
printinfo(name="zhangsan", age=50)
printinfo(name="lisi")


#可写函数说明
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return
 
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")




