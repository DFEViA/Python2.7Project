#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-24 10:15:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

def test():
	pass


if __name__ == '__main__':#__name__是指当前py文件调用方式的方法。如果它等于“__main__”就表示是直接执行，如果不是，则用被别的文件滴啊用，这个死后if就为False，那么他就不会执行最外层的代码了。
	line = 'say hello world hi'
	parts = line.split(' ', 3)
	print parts

