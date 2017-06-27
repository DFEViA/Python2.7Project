#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-06-27 16:39:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

print ('Content-type: text/html\n')
import cgitb; cgitb.enable()

import psycopg2
conn = psycopg2.connect('dbname=test user=postgres')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()
id = form.getvalue('id')

print("""
<html>
  <head>
    <title>View Message</title>
  </head>
  <body>
    <h1>View Message</h1>
"""	)
try:
	id = int(id)
except:
	print ('Invalid message ID')
	sys.exit()

curs.execute('SELECT * FROM messages WHERE id = %i' % id)
rows = curs.fetchall()

if not rows:
	print ('Unkonwn message ID')
	sys.exit()

row = rows[0]

temp = {}
temp['id'] = row[0]
temp['subject'] = row[1]
temp['sender'] = row[2]
temp['reply_to'] = row[3]
temp['text'] = row[4]

print("""
	<p><b>Subject:</b> %(subject)s<br />
	<b>Sender:</b> %(sender)s<br />
	<pre>%(text)s</pre>
	</p>
	<hr />
	<a href='main.cgi'>Back to the main page</a>
	|<a href="edit.cgi?reply_to=%(id)s">Reply</a>
  </body>
</html>
	""" % temp)