#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 文本块生成器

#注意file.read()和标准输入sys的文件不一样，一个逐个字符读取，一个逐行读取

def lines(file):
    for line in file:
        yield line
    yield '\n'# 结束生成器，生成器可用for循环迭代


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()  # 连接字符串
            block = []

