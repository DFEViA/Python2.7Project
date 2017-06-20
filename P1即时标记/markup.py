#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 21:34:54
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import sys, re
from handlers import *
from util import *
from rules import *

class Parser:
	""" 
	语法分析器读取文本文件、应用规则并且控制处理程序
	"""
	def __init__(self, handler):
	    self.handler = handler
	    self.rules = []# 规则器
	    self.filters = []# 过滤器
	def addRule(self, rule):
		self.rules.append(rule)
	def addFilter(self, pattern, name):
		def filter(block, handler):
			return re.sub(pattern, handler.sub(name), block)
	"""
	 	然后仔细看书，书上在前面有这样一句话，[re.sub函数可以将第一个函数作为第二个参数]。至少笔者觉得这句话写的很奇怪，’第一个函数‘明明要写成第一个参数啊有木有。好吧，不吐槽这些。
　　 大概意思就是，re.sub的第二个参数可以是一个函数作为替换式，替换式的参数就是re.sub的第一个参数匹配后返回的正则对象。
　　 	这下就可以看懂了，我们会去调用sub_emphasis(self,match)，然后match.group(1)表示的实际上是is。关于group(1)大家去看一下，re模块的内容，在这里我就直接告诉你他的内容，就是匹配式(.+?)中的内容。
	"""
		self.filters.append(filter)
	def parse(self, file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters:
				block = filter(block, self.handler)#重新绑定到block
			for rule in self.rules:
				if rule.condition(block):
					last = rule.action(block, self.handler)
					if last:break
		self.handler.end('document')

class BasicTestParser(Parser):
	"""
	在构造函数中增加规则和过滤器的具体语法分析器
	"""
	def __init__(self, handler):
		Parser.__init__(self, handler)
		self.addRule(ListRule())
		self.addRule(ListItemRule())
		self.addRule(TitleRule())
		self.addRule(HeadingRule())
		self.addRule(ParagraphRule())

		self.addFilter(r'\*(.+?)\*', 'emphasis')
		self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
		self.addFilter(r'([\.a-zA-z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRenderer()
parser = BasicTestParser(handler)

parser.parse(sys.stdin)