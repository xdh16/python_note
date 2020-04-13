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
tuple1[2] = 1000 #元组不能修改值

