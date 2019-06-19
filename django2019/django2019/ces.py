# import pymysql
# connection = pymysql.connect(host='127.0.0.1',
# user='root',
# password='321100',
# db='djangwy',
# charset='utf8mb4',
# cursorclass=pymysql.cursors.DictCursor)
import re
# s2 = 'abc4efg'
# m = re.search('^[a-z]+$', s2)
# print(m)
# def fab(n):
#     a,b=0,1
#     for i in range(n):
#         yield b
#         a,b=b,a+b
#
#     return "done!"
# l=fab(6)
# while True:
#     try:
#         print(next(l))
#     except StopIteration as e:
#         print(e)
#         break

#
# l=[2,33,1,6,99,22]
# def maopao(l):
#     for i in range(len(l)-1):
#         for j in range(len(l)-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l
# print(maopao(l))
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%2d"%(i,j,i*j),end=" ")
#     print("")
# info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# info=map(lambda x:x+1,info)
# print(list(info))

import time
l= time.strptime("2019-06-22 07:03:06", "%Y-%m-%d %H:%M:%S")
t=time.mktime(l)
print(t)
data={"xiaoming":15,"xiaohong":"女","xiaogang":"xuesheng"}
# for key,value in data.items():
'''for key in data:
    data[key]=str(data[key])
print(data)
key=",".join(data.keys())
print(key)
value=",".join(data.values())
print(value)
real_sql="insert into " +"students" +"("+key+")"+"values"+"("+value+")"
print(real_sql)'''

import time
def consumer(name):
    print("%s 准备学习啦!" %name)
    while True:
       lesson = yield

       print("开始[%s]了,[%s]老师来讲课了!" %(lesson,name))
a=consumer("xiaoming")

a.__next__()
