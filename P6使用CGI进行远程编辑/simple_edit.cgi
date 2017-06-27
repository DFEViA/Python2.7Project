#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()

# 没有输入内容时，默认显示open('simple_edit.dat').read()内容
text = form.getvalue('text', open('simple_edit.dat').read())
print text
f = open('simple_edit.dat', 'w')
f.write(text)
f.close()
print """Content-type: text/html

<html>
  <head>
    <title>A Simple Editor</title>
  </head>
  <body>
  	<form action='simple_edit.cgi' method='Post'>
  	<textarea rows='10' cols='20' name='text'>%s</textarea><br />
  	<input type='submit' />
  	</from>
  </body>
</html>
""" % text