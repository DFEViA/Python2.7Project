#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-19 21:33:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# graphics 制图学
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello, world!', textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')
