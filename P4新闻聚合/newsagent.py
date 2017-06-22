#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 11:26:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

from nntplib import NNTP
from time import strftime, time, localtime

day = 24 * 60 * 60

yesterday = localtime(time() - day)
date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

servername = 'news2.neva.ru'
group = 'alt.sex.telephone'
#group = 'comp.lang.python.announce'
server = NNTP(servername)

ids = server.newnews(group, date, hour)[1]
print ids

for id in ids:
	head = server.head(id)[3]
	for line in head:
		if line.lower().startswith('subject:'):
			subject = line[9:]
			break

	body = server.body(id)[3]

	print subject
	print '-'*len(subject)
	print '\n'.join(body)

server.quit()