#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-29 17:34:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from xmlrpc.client import ServerProxy, Fault
from os.path import join, abspath, isfile
from xmlrpc.server import SimpleXMLRPCServer
from urllib.parse import urlparse
import sys

SimpleXMLRPCServer.allow_reuse_address = 1

MAX_HISTORY_LENGTH = 6

UNHANDLED = 100
ACCESS_DENIED = 200

class UnhandleQuery(Fault):
	"""
	表示无法处理的查询的异常。
	"""
	def __init__(self, message="Couldn't handle the query"):
	    Fault.__init__(self, UNHANDLED, message)

class AccessDenied(Fault):
	"""
	在用户视图访问未被授权访问的资源时引发的异常。
	"""
	def __init__(self, message="Access denied"):
		Fault.__init__(self, ACCESS_DENIED, message)

#注意下如何调用的
def inside(dir, name):
	"""
	检查给定的目录中是否有给定的文件名。
	"""
	name = join(dir, name)
	dir = abspath(dir)
	name = abspath(name)
	return name.startswith(join(dir, ''))

def getPort(url):
	"""
	从URL中提取端口号
	"""
	name = urlparse(url)[1]
	parts = name.split(':')
	return int(parts[-1])

class Node:
	"""
	P2P网络中的节点
	"""
	def __init__(self, url, dirname, secret):
		self.url = url
		self.dirname = dirname
		self.secret = secret
		self.konwn = set()
	
	def query(self, query, history=[]):
		"""
		查询文件，可能会向其他已知几点请求帮助。将文件作为字符串返回
		"""
		try:
			return self._handle(query)
		except UnhandleQuery:
			history = history + [self.url]
			if len(history) >= MAX_HISTORY_LENGTH: raise
			return self._broadcast(query, history)

	def hello(self, other):
		"""
		用于将节点介绍给其他节点。
		"""
		self.konwn.add(other)
		print(self.konwn)
		return 0

	def fetch(self, query, secret):
		"""
		用于让节点找到文件并且下载。
		"""
		if secret != self.secret: raise AccessDenied
		result = self.query(query)
		f = open(join(self.dirname, query),'w')
		print(join(self.dirname, query))
		print(f)
		print(result)
		f.write(result)
		f.close()
		return 0

	def _start(self):
		"""
		内部使用，以启动XML_RPC服务器
		"""
		s = SimpleXMLRPCServer(("", getPort(self.url)), logRequests = False)
		s.register_instance(self)
		s.serve_forever()

	def _handle(self, query):
		"""
		内部使用，用于处理请求
		"""	
		dir = self.dirname
		name = join(dir, query)
		if not isfile(name): raise UnhandleQuery
		if not inside(dir, name): raise AccessDenied
		return open(name).read()

	def _broadcast(self, query, history):
		"""
		内部使用，用于将查询广播到所有已知节点。
		"""
		for other in self.konwn.copy():
			if other in history: continue
			try:
				s = ServerProxy(other)
				return s.query(query, history)
			except:
				self.konwn.remove(other)
		raise UnhandledQuery

def main():
	url, directory, secret = sys.argv[1:]
	n = Node(url, directory, secret)
	n._start()

if __name__ == '__main__':
	main()