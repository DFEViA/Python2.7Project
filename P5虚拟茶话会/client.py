#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-24 13:35:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


#客户端连接服务器使用了telnetlib模块

import wx
import telnetlib
from time import sleep
import thread
import test

class LoginFrame(wx.Frame):
	"""
	登录窗口
	"""
	def __init__(self, parent, id, title, size):
		'初始化， 添加控件并绑定事件'
		wx.Frame.__init__(self, parent, id, title)

