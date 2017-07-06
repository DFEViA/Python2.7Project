#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-06-29 13:08:14
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

'''
from urllib.parse import urlparse

def getPort(url):
	'用URL中提取端口'
	name = urlparse(url)[1]
	print (name)
	parts = name.split(':')
	print (parts)
	return int(parts[-1])

print(getPort('http://localhost:4242'))
'''

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

#当for语句中没有执行break的话，遍历完for语句，就会执行else语句
#但是如果中间执行了break语句，跳出for循环，那么不会执行else语句。

'''
import os
from os.path import join, abspath, isfile



def inside(dir, name):
	"""
	检查给定的目录中是否有给定的文件名。
	"""
	name = join(dir,name)
	dir = abspath(dir)
	print(dir)
	name = abspath(name)
	print(name)
	print(isfile(name))
	return name.startswith(join(dir,''))

print(inside('files1', 'test.txt'))
'''



