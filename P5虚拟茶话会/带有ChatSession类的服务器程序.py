#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 17:38:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5006

class ChatSession(async_chat):
	"""docstring for ChatSession"""
	def __init__(self, sock):
		async_chat.__init__(self, sock)
		self.set_terminator("\r\n")
		self.data = []

	def collect_incoming_data(self, data):
		self.data.append(data)

	def found_terminator(self):
		line = ''.join(self.data)
		self.data = []
		#处理这行数据......
		print line

class ChatServer(dispatcher): 

	def __init__(self, port):
		dispatcher.__init__(self)
		#使用指定所需套接字类型的两个参数
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		#调用bind方法会把服务器绑定到具体的地址上（主机名和端口）
		self.bind(('', port))
		#调用listen以告诉服务器要监听连接，并且指定5个连接的待办的事务。
		self.listen(5)
		self.sessions = []
	    
	def handle_accept(self):
		conn, addr = self.accept()
		self.sessions.append(ChatSession(conn))
		
if __name__ == '__main__':
	s = ChatServer(PORT)
	try:
		asyncore.loop()
	except KeyboardInterrupt:
		print
