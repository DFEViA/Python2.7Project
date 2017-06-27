#!/usr/bin/python3
# @Date    : 2017-06-26 11:08:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import psycopg2

conn = psycopg2.connect('user=postgres dbname=test')
curs = conn.cursor()

#print (psycopg2.__file__)

"""
curs.execute('SELECT * FROM messages')
print(curs.fetchall())

curs.execute("INSERT INTO messages VALUES (1,'a','a',1,'a')")

#先执行一条SQL
curs.execute('SELECT * FROM messages')
print(curs.fetchall())#拿到结果后，再次执行此语句，结果就为空了；
print(curs.fetchone())
"""

reply_to = input('Reply to: ')
subject = input('Subject: ')
sender = input('Sender: ')
text = input('Text: ')

if reply_to:
	query = """
	INSERT INTO messages(reply_to, sender, subject, text)
	VALUES(%s, '%s', '%s', '%s')""" % (int(reply_to), sender, subject, text)
else:
	query = """
	INSERT INTO messages(sender, subject, text)
	VALUES('%s', '%s', '%s')""" % (sender, subject, text)

curs.execute(query)
conn.commit()

curs.execute('SELECT * FROM messages')
print(curs.fetchall())  # 拿到结果后，再次执行此语句，结果就为空了；
