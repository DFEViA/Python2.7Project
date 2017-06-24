#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 16:35:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from asyncore import dispatcher
import asyncore, socket

PORT = 5005

class ChatServer(dispatcher): 

	def __init__(self, port):
		dispatcher.__init__(self)
		#使用指定所需套接字类型的两个参数
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		#新增的对应set_reuse_addr的调用可以在服务器没有正确关闭的情况下重用同一个地址
		self.set_reuse_addr()
		#调用bind方法会把服务器绑定到具体的地址上（主机名和端口）
		self.bind(('', port))
		#调用listen以告诉服务器要监听连接，并且指定5个连接的待办的事务。
		self.listen(5)
	    
	def handle_accept(self):
		conn, addr = self.accept()
		print 'Connection attempt from', addr[0]#是客户端的IP地址

if __name__ == '__main__':
	s = ChatServer(PORT)
	try:
		asyncore.loop()
	except KeyboardInterrupt:
		pass
			