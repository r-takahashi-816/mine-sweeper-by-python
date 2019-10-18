import sys
import pygame
from globals import *
from create_iterator import CreateIterator

class GUIManager:
	def __init__(self,setting,title="",debug=False):
		pygame.init()
		pygame.display.set_caption(title)

		self.setting = setting
		self.field = self.setting.field
		self.width = self.setting.width
		self.height = self.setting.height
		self.window_size = (self.width*SIZE,self.height*SIZE)
		self.surface = pygame.display.set_mode(self.window_size)
		self.fpsclock = pygame.time.Clock()
		self.smallfont = pygame.font.SysFont(None,36)
		self.largefont = pygame.font.SysFont(None,72)
		
		message_color = (255,255,0)
		self.message_clear = self.get_font_image("CLEAR!",color=message_color,large=True)
		self.message_over = self.get_font_image("GAME OVER!",color=message_color,large=True)
		self.message_rect = self.message_clear.get_rect()
		self.message_rect.center = (self.width*SIZE/2,self.height*SIZE/2)
		self.debug = debug

		strip = pygame.image.load("img/bomb.png")
		bomb_image = pygame.Surface((32,32))
		bomb_image.blit(strip,(0,0),pygame.Rect((0,0),(32,32)))
		self.bomb_image = pygame.transform.scale(bomb_image,(50,50))
	
	def get_font_image(self,msg,color=(255,255,255),large=False):
		if large :
			return self.largefont.render("{}".format(msg),True,color)
		return self.smallfont.render("{}".format(msg),True,color)

	def draw_board(self,game_logic):
		self.draw_tile(game_logic)
		self.draw_lattice()
		self.draw_message(game_logic)
		pygame.display.update()
		self.fpsclock.tick(15)

	def draw_tile(self,game_logic):
		dark_color = (50,50,50)
		gray_color = (70,70,70)
		num_color = (255,255,0)

		self.surface.fill(gray_color)
		pos_iter = CreateIterator.create(range(self.width),range(self.height))

		for xpos,ypos in pos_iter():
			tile = self.field[ypos][xpos]
			rect = (xpos*SIZE,ypos*SIZE,SIZE,SIZE)
			
			# タイルの描写
			if tile == EMPTY or tile == BOMB :
				pygame.draw.rect(self.surface,dark_color,rect)

				# 地雷の描写
				if (game_logic.game_over and tile == BOMB) or (self.debug and tile == BOMB):
					self.surface.blit(self.bomb_image,rect)

			elif tile == OPENED:
				count = game_logic.get_bombs_number(xpos,ypos)
				if count > 0 :
					num_image = self.get_font_image("{}".format(count),color=num_color)
					self.surface.blit(num_image,(xpos*SIZE+10,ypos*SIZE+10))

	def draw_lattice(self):
		line_color = (96,96,96)
		for index in range(0,self.width*SIZE,SIZE):
			pygame.draw.line(self.surface,line_color,(index,0),(index,self.height*SIZE))
		for index in range(0,self.height*SIZE,SIZE):
			pygame.draw.line(self.surface,line_color,(0,index),(self.width*SIZE,index))

	def draw_message(self,game_logic):
		if game_logic.is_clear():
			self.surface.blit(self.message_clear,self.message_rect.topleft)
		elif game_logic.game_over:
			self.surface.blit(self.message_over,self.message_rect.topleft)