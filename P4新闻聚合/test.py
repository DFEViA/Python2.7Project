#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 10:02:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


#print '1111'

# python test.py >> a.txt 将标准输出（print）写入文件


from nntplib import NNTP
from time import time, localtime, strftime

day = 24 * 60 * 60# Number of seconds in one day
print time()# 打印当前时间
yesterday = localtime(time() - day)# 减去一天，获取昨天的时间
print yesterday

date = strftime('%y%m%d')
hour = strftime('%H%M%S')

print date, hour

date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

print date, hour

servername = 'news2.neva.ru'
group = 'alt.sex.telephone'

server = NNTP(servername)
ids = server.newnews(group, date, hour)[1]



