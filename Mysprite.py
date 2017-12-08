#!/usr/bin/python3
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *

class Mysprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.master_image=None
		self.width=0
		self.height=0
		self.row=0
		self.col=0

	def _getx(self):
		return self.rect.x
	def _setx(self,value):
		self.rect.x=value
	X=property(_getx,_setx)

	def _gety(self):
		return self.rect.y
	def _sety(self,value):
		self.rect.y=value
	Y=property(_gety,_sety)

	def _getpos(self):
		return self.rect.topleft
	def _setpos(self,pos):
		self.rect.topleft=pos
	position=property(_getpos,_setpos)


	def trans(self):
		self.master_image=pygame.transform.smoothscale(self.master_image,(self.width//4,self.height//4))

	def load(self,filename):
		self.master_image=pygame.image.load(filename).convert_alpha()
		self.width,self.height=self.master_image.get_size()
		self.rect=Rect(0,0,self.width,self.height)

	def set_image(self,image):
		self.master_image=image
		self.width,self.height=image.get_size()
		self.rect=Rect(0,0,self.width,self.height)

	def update(self):
		self.image=self.master_image


