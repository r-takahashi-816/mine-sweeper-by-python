import pygame
from globals import *
from setting_manager import SettingManager
from gui_manager import GUIManager
from event_listener import EventListener
from game_logic import GameLogic

class MineSweeper:
	def __init__(self,args):
		mode = "easy"
		if args.normal :
			mode = "normal"
		elif args.sticky :
			mode = "hard"
		self.setting = SettingManager(mode=mode)
		self.game_logic = GameLogic(self.setting)
		self.gui = GUIManager(self.setting,title="Mine Sweeper",debug=args.debug)
		self.event_listener = EventListener(self.setting)
		
	def loop(self):
		while True:
			listener_return = self.event_listener.listen(pygame.event.get())
			self.game_logic.listener_receive(listener_return)
			self.gui.draw_board(self.game_logic)