from globals import *
from random import randint
from create_iterator import CreateIterator

class GameLogic:
	def __init__(self,setting,num_of_bombs=20):
		self.setting = setting
		self.game_over = False
		self.open_count = 0
		self.num_of_bombs = self.setting.num_of_bombs
		self.field = self.setting.field
		self.width = self.setting.width
		self.height = self.setting.height
		self.checked = self.setting.CHECKED
		self.set_bombs()

	def is_clear(self):
		return self.open_count == self.width*self.height - self.num_of_bombs

	def in_field(self,xpos,ypos):
		return 0 <= xpos < self.width and 0 <= ypos < self.height

	def set_bombs(self):
		count = 0
		while count < self.num_of_bombs:
			xpos,ypos = randint(0,self.width-1),randint(0,self.height-1)
			if self.field[ypos][xpos] == EMPTY:
				self.field[ypos][xpos] = BOMB
				count += 1

	def get_bombs_number(self,x_pos,y_pos):
		"""周囲にある爆弾の数を返す"""
		count = 0
		offset_iter = CreateIterator.create(range(-1,2),range(-1,2))
		for xoffset,yoffset in offset_iter():
			xpos,ypos = (x_pos+xoffset,y_pos+yoffset)
			if self.in_field(xpos,ypos) and self.field[ypos][xpos] == BOMB:
				count += 1
		return count

	def open_tile(self,x_pos,y_pos):
		if self.checked[y_pos][x_pos]:
			return
		self.checked[y_pos][x_pos] = True
		
		offset_iter = CreateIterator.create(range(-1,2),range(-1,2))
		for xoffset,yoffset in offset_iter():
			xpos,ypos = (x_pos+xoffset,y_pos+yoffset)
			if self.in_field(xpos,ypos) and self.field[ypos][xpos] == EMPTY:
				self.field[ypos][xpos] = OPENED
				self.open_count += 1
				count = self.get_bombs_number(xpos,ypos)

				if count == 0 and not(xpos == x_pos and ypos == y_pos):
					self.open_tile(xpos,ypos)
						
	def listener_receive(self,rets):
		if rets != None and type(rets) != bool and len(rets)>=2:
			xpos,ypos = rets[0],rets[1]
			self.open_tile(xpos,ypos)
		elif rets != None and rets:
			self.game_over = True
	
