#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-06-27 15:53:27
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

print ('Content-type: text/html\n')

import cgitb; cgitb.enable()

import psycopg2
conn = psycopg2.connect('dbname=test user=postgres')
curs = conn.cursor()

print ("""
  <html>
    <head>
      <title>The FooBar Bullet in Board</title>
    </head>
    <body>
      <h1>The FooBar Bulletin Board</title>
"""
)

curs.execute('SELECT * FROM messages')
rows = curs.fetchall()
toplevel = []
children = {}

for row in rows:
  	parent_id = row[3]
  	if parent_id is None:
  		toplevel.append(row)
  	else:
   		children.setdefault(parent_id,[]).append(row)#value是一个列表，append是往列表增加元素

print(children)

def format(row):

	temp = {}
	temp['id'] = row[0]
	temp['subject'] = row[1]
	print ('<p><a href="view.cgi?id=%(id)i">%(subject)s</a></p>' % temp)
	try:
  		kids = children[row[0]]
	except KeyError:
  		pass
	else:
		print ('<blockquote>')
		for kid in kids:
  			format(kid)
		print ('</blockquote>')

print ('<p>')
for row in toplevel:
  	format(row)
print ("""
    </p>
  </body>
</html>
""")