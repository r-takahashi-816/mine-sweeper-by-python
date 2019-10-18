
from globals import *
import sys
import pygame
from pygame.locals import QUIT,MOUSEBUTTONDOWN

event_registory = {}
def register(key):
	def _decorator(func):
		event_registory[key] = func
		def inner(*args,**kwargs):
			ret = func(*args,**kwargs)
			return ret
		return inner
	return _decorator

class EventListener:
	def __init__(self,setting):
		self.setting = setting

	def listen(self,events):
		ret = None
		for event in events:
			if event.type == QUIT:
				ret = event_registory["quit"]()
			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				ret = event_registory["click"](event,self.setting.field)
		return ret

@register(key="quit")
def quit():
	pygame.quit()
	sys.exit()

from math import floor
@register(key="click")
def click_tile(event,field):
	xpos,ypos = floor(event.pos[0]/SIZE),floor(event.pos[1]/SIZE)
	if field[ypos][xpos] == BOMB :
		return True
	else :
		return xpos,ypos