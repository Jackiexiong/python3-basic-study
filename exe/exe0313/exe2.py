#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   exe2.py
@Time    :   2020/03/12 09:49:29
@Author  :   Jackiex 
@Version :   1.0
'''
'''
  2 一个字典中，存放了10个学生的学号（key）和分数（value）；
  请筛选输出，大于80分的同学（按照格式：学号：分数）；
'''
stu = {             # 对于字典的初始化,我们需要排版好格式
   '101' : 80,
   '102' : 76,
   '103' : 80,
   '104' : 76,
   '105' : 81,
   '106' : 73,
   '107' : 88,
   '108' : 70,
   '109' : 88,
   '110' : 70,
}


print("学号--分数")
for k,v in stu.items():  
    if v>=80:
      print(k,"--",v)

