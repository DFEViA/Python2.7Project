#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-21 17:07:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

from xml.sax.handler import ContentHandler
from xml.sax import parse


# 调度类
class Dispatcher:
	"""docstring for Dispatch"""

	def dispatch(self, prefix, name, attrs=None):
		mname = prefix + name.capitalize()  # 字符串首字母大写
		dname = 'default' + prefix.capitalize()
		method = getattr(self, mname, None)
		if callable(method): args = ()
		else:
			method = getattr(self, dname, None)
			args = name,
		if prefix == 'start': 
			args += attrs, 
		if callable(method): method(*args)# 星号形式可以传多个参数

	def startElement(self, name, attrs):
		self.dispatch('start', name, attrs)

	def endElement(self, name):
		self.dispatch('end', name)


class WebsiteConstructor(Dispatcher, ContentHandler):
	passthrough = False

	def __init__(self, directory):
		self.directory = [directory]
		self.ensureDirectory()

	# 判断目录是否存在，不存在创建目录
	def ensureDirectory(self):
		path = os.path.join(*self.directory)  # 一个序列有多个元素，使用*号进行参数分割
		if not os.path.isdir(path): os.makedirs(path)

	def characters(self, chars):
		if self.passthrough: self.out.write(chars)

	def defaultStart(self, name, attrs):
		if self.passthrough:
			self.out.write('<' + name)
			for key, val in attrs.items():# attrs.items()为空，for循环不执行
				self.out.write(' %s="%s"' % (key, val))
			self.out.write('>')# 注意缩进，缩进错误可能不会报缩进错误
	
	def defaultEnd(self, name):
		if self.passthrough:
			self.out.write('</%s>' % name)

	def startDirectory(self, attrs):
		self.directory.append(attrs['name'])
		self.ensureDirectory()

	def endDirectory(self):
		self.directory.pop()#移除列表元素（默认最后一个元素）

	def startPage(self, attrs):
		filename = os.path.join(*self.directory+[attrs['name']+'.html'])
		self.out = open(filename, 'w')
		self.writeHeader(attrs['title'])
		self.passthrough = True

	def endPage(self):
		self.passthrough = False
		self.writeFooter()
		self.out.close()

	def writeHeader(self, title):
		self.out.write('<html>\n <head>\n <title>')
		self.out.write(title)
		self.out.write('</title>\n </head>\n  <body>\n')

	def writeFooter(self):
		self.out.write('\n </body>\n</html>\n')

parse('website.xml', WebsiteConstructor('public_html'))
