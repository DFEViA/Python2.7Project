#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-28 10:58:14
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from xmlrpc.client import ServerProxy
mypeer = ServerProxy('http://localhost:4343')#第二个点
code, data = mypeer.query('test.txt')
print(code)
print(data)

otherpeer = ServerProxy('http://localhost:4344')#第二个点
code, data = otherpeer.query('test.txt')
print(code)
print(data)

mypeer.hello('http://localhost:4344')#将mypeer介绍给otherpeer
code, data = mypeer.query('test.txt')
print(code)
print(data)

mypeer.fetch('test.txt', 'secrect1')