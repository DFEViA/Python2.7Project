#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-04 18:22:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pygame, config, os
from random import randrange

#这个模块包括Squish的游戏对象。
class SquishSprite(pygame.sprite.Sprite):
	"""
	Squish中所有子图形的范型超类。构造函数负责载入图像，设置子图形的rect和area属性。
	并且允许它在指定区域内进行移动。area由屏幕的大小和留百决定。
	"""
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image).convert()
		self.rect = self.image.get_rect()#rect函数
		screen = pygame.display.get_surface()
		shrink = -config.margin*2
		self.area = screen.get_rect().inflate(shrink, shrink)

class Weight(SquishSprite):
	"""
	落下的秤砣。它使用了SquishSprite的构造函数设置它的秤砣图像，并且会以给定的速度作为构造函数的参数来设置下落的速度
	"""
	def __init__(self, speed):
		SquishSprite.__init__(self, config.weight_image)
		self.speed = speed
		self.reset()

	def reset(self):
		"""
		将秤砣移动到屏幕顶端（视线外），放置到任意水平位置下。
		"""
		x = randrange(self.area.left, self.area.right)#在给定参数返回一个随机数
		self.rect.midbottom = x, 0

	def update(self):
		"""
		根据它的速度将秤砣垂直移动一段距离。并且根据它是否处理屏幕地段来设置landed属性。
		"""	
		self.rect.top += self.speed
		self.landed = self.rect.top >= self.area.bottom

class Banana(SquishSprite):
	"""
	绝望的香蕉，它使用SquishSprite构造函数设置香蕉的图像，并且会停留在屏幕地段。
	"""
	def __init__(self):
		SquishSprite.__init__(self, config.banana_image)
		self.rect.bottom = self.area.bottom
		#在没有香蕉的部分进行填充。
		#如果秤砣移动到了这些区域，它不会
		#被判定为碰撞（或者说是将香蕉压扁）；
		self.pad_top = config.banana_pad_top
		self.pad_side = config.banana_pad_side

	def update(self):
		"""
		将Banana中心点的横坐标设定为当前鼠标指针的横坐标，并且使用rect的clamp方法确保Banana停留在所允许的范围内。
		"""
		self.rect.centerx = pygame.mouse.get_pos()[0]
		self.rect = self.rect.clamp(self.area)

	def touches(self, other):
		"""
		确定香蕉是否触碰到了另外的子图形（比如秤砣）。除了使用rect的colliderect方法外，首先要计算一个不包括香蕉图形
		像顶端和侧边“空区域”的新矩形（使用rect的inflate方法对顶端和侧边进行填充）。
		"""
		# 使用适当的填充缩小边界：
		bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
		# 移动边界，将他们放置到Banana的底部。
		bounds.bottom = self.rect.bottom
		# 检查边界是否和其他对象的rect交叉
		return bounds.colliderect(other.rect)