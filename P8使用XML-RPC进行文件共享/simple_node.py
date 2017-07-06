#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-06-28 16:58:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer
from os.path import join, isfile
from urllib.parse import urlparse
import sys

MAX_HISTORY_LENGTH = 6

OK = 1
FAIL = 2
EMPTY = ''

def getPort(url):
	'用URL中提取端口'
	name = urlparse(url)[1]
	parts = name.split(':')
	return int(parts[-1])

class Node:
	"""
	P2P网络中的节点
	"""
	#构造方法
	def __init__(self, url, dirname, secrect):
		self.url = url
		self.dirname = dirname
		self.secrect = secrect
		self.konwn = set()

	def query(self, query, history=[]):
		"""
		查询文件，可能会向其他已知节点请求帮助，将文件作为字符串返回
		"""
		code, data = self._handle(query)
		if code == OK:
			return code, data
		else:
			history = history + [self.url]
			if len(history) >= MAX_HISTORY_LENGTH:
				return FAIL, EMPTY
			return self._broadcast(query, history)

	def hello(self, other):
		"""
		用于将节点介绍给其他节点:
		"""
		self.konwn.add(other)
		return OK
	def fetch(self, query, secrect):
		"""
		用于让节点找到文件并且下载
		"""
		if secrect != self.secrect: return FAIL
		code, data = self.query(query)
		if code == OK:
			f = open(join(self.dirname, query), 'w')#读取文件，写入本地文件
			f.write(data)
			f.close()
			return OK
		else:
			return FAIL
	def _start(self):
		"""
		内部使用，用于启动XML_RPC服务器
		"""
		s = SimpleXMLRPCServer(("", getPort(self.url)), logRequests=False)
		s.register_instance(self)#注册一个实例
		s.serve_forever()

	def _handle(self, query):
		"""
		内部使用，用于处理请求。
		"""
		dir = self.dirname
		name = join(dir, query)#文件相对路径
		if not isfile(name):return FAIL, EMPTY
		return OK, open(name).read()

	def _broadcast(self, query, history):
		"""
		内部使用，用于将查询广播到所有已知Node。
		"""
		for other in self.konwn.copy():#拷贝已知节点
			if other in history: continue#如果存在请求历史
			try:
				s = ServerProxy(other)
				code, data = s.query(query, history)
				if code == OK:
					return code, data
			except:
				self.konwn.remove(other)
		return FAIL, EMPTY

def main():
	url, directory, secrect = sys.argv[1:]
	n = Node(url, directory, secrect)
	n._start()

if __name__ == '__main__':
	main()