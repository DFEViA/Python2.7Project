#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-06-28 10:36:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from xmlrpc.server import SimpleXMLRPCServer

s = SimpleXMLRPCServer(('', 4242))# 使用Localhost，端口4242
def twice(x):# 实例函数
	return x*2

s.register_function(twice)# 向服务器添加功能
s.serve_forever()# 启动服务器

