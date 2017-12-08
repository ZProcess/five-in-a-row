#!/usr/bin/python3
#-*- coding:utf-8 -*-

import pygame,sys,time
from pygame.locals import *
from Mysprite import *


pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Five-in-a-row")

myfont=pygame.font.Font(None,60)

panel_lefttop_x=53
panel_lefttop_y=33
sq_len=35

chess_lefttop_x=63
chess_lefttop_y=43

panel=Mysprite()
panel.load("panel.png")
panel.X=50
panel.Y=30
panel_group=pygame.sprite.Group()
panel_group.add(panel)
panel_group.update()
panel_group.draw(screen)

chess_group=pygame.sprite.Group()

image=pygame.Surface((19,19)).convert_alpha()
image.fill((255,255,255,0))
for n in range(0,15):
	for m in range(0,15):
		chess=Mysprite()
		chess.set_image(image)
		chess.X=chess_lefttop_x+sq_len*m
		chess.Y=chess_lefttop_y+sq_len*n
		chess.row=n
		chess.col=m
		chess_group.add(chess)

def chess_image(filename):
	chess_image=pygame.image.load(filename).convert_alpha()
	width,height=chess_image.get_size()
	chess_image=pygame.transform.smoothscale(chess_image,(width//4,height//4))
	return chess_image

white=chess_image("white.jpg")
black=chess_image("black.jpg")

cursor_image=pygame.Surface((5,5)).convert_alpha()
cursor_image.fill((0,0,0))
cursor=Mysprite()
cursor.set_image(cursor_image)

class five_chess():
	def __init__(self):
		self.chess_map=[]
		self.numb_in_line=1

	def map_init(self):
		for n in range(0,23):
			row=[]
			for m in range(0,23):
				row.append(0)
			self.chess_map.append(row)
			
	def is_win(self,current_x,current_y,chess_color):
		n=1
		m=1
		self.numb_in_line=1
        # first circustance
		while n<=4 and self.chess_map[current_x-n][current_y]==chess_color:
			self.numb_in_line+=1
			n+=1
		while m<=4 and self.chess_map[current_x+m][current_y]==chess_color:
			self.numb_in_line+=1
			m+=1
		if self.numb_in_line==5:
			return True
		else:
			n=1
			m=1
			self.numb_in_line=1
		# second circustance
		while n<=4 and self.chess_map[current_x][current_y-n]==chess_color:
			self.numb_in_line+=1
			n+=1
		while m<=4 and self.chess_map[current_x][current_y+m]==chess_color:
			self.numb_in_line+=1
			m+=1
		if self.numb_in_line==5:
			return True
		else:
			n=1
			m=1
			self.numb_in_line=1
		# third circustance
		while n<=4 and self.chess_map[current_x-n][current_y+n]==chess_color:
			self.numb_in_line+=1
			n+=1
		while m<=4 and self.chess_map[current_x+m][current_y-m]==chess_color:
			self.numb_in_line+=1
			m+=1
		if self.numb_in_line==5:
			return True
		else:
			n=1
			m=1
			self.numb_in_line=1
		# fourth circustance
		while n<=4 and self.chess_map[current_x-n][current_y-n]==chess_color:
			self.numb_in_line+=1
			n+=1
		while m<=4 and self.chess_map[current_x+m][current_y+m]==chess_color:
			self.numb_in_line+=1
			m+=1
		if self.numb_in_line==5:
			return True
		else:
			n=1
			m=1
			self.numb_in_line=1

c_x=0
c_y=0
current_color=1
player=five_chess()
player.map_init()


color_dict={1:"black",2:"white"}

def print_result(color):
	text=str(color_dict[color])+" is five in a row "
	text_image=myfont.render(text,True,(255,255,255))
	screen.blit(text_image,(200,100))

def print_template(*argv):
	text=""
	for n in argv:
		text=text+str(n)
	text_image+myfont.render(text,True,(255,255,255))
	screen.blit(text_image,(200,100))

is_finish=False

while True:
	keys=pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()
	for event in pygame.event.get():
		if event.type==QUIT:
			sys.exit()
		elif event.type==MOUSEBUTTONDOWN:
			cursor.X,cursor.Y=event.pos
			collide_list=pygame.sprite.spritecollide(cursor,chess_group,True)
			if collide_list:
				map_x=collide_list[-1].col
				map_y=collide_list[-1].row
				c_x=collide_list[-1].col*35+53
				c_y=collide_list[-1].row*35+33
				if current_color==1:
					screen.blit(black,(c_x,c_y))
					player.chess_map[4+map_x][4+map_y]=1
					current_color=2
					if player.is_win(4+map_x,4+map_y,1):
						print_result(1)
						is_finish=True
				elif current_color==2:
					screen.blit(white,(c_x,c_y))
					player.chess_map[4+map_x][4+map_y]=2
					current_color=1
					if player.is_win(4+map_x,4+map_y,2):
						print_result(2)
						is_finish=True
	

	pygame.display.update()
	if is_finish:
		break

while True:
	pass

