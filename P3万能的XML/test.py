#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-20 13:20:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

'''import os

from xml.sax.handler import ContentHandler# 内容处理程序
from xml.sax import parse

class HeadlineHandler(ContentHandler):
	"""docstring for HeadlineHandler"""
	in_headline = False
	def __init__(self, headlines):
		ContentHandler.__init__(self)
		self.headlines = headlines
		self.data = []

	#读取开始标签
	def startElement(self, name, attrs):
		if name == 'h1':
			self.in_headline = True
		for key, val in attrs.items():
			print key,val

	#读取结束标签
	def endElement(self, name):
		if name == 'h1':
			text = ''.join(self.data)
			self.data = []
			self.headlines.append(text)
			self.in_headline = False

	#characters方法会在语法分析器找到一些文本时自动被调用
	def characters(self, string):
		if self.in_headline:#这类方法（使用布尔变量来判断你当前是否位于给定标签类型内）在SAX程序设计非常普遍
			self.data.append(string)
		

headlines = []
parse('website.xml', HeadlineHandler(headlines))

print 'The following <h1> elements were found:'
for h in headlines:
	print h'''

for i in ():
	print i


		




			