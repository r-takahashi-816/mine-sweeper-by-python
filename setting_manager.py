class SettingManager:
	def __init__(self,mode):
		self.mode = mode
		self.difficulty = {"easy":20,"normal":40,"hard":100}
		self.num_of_bombs = self.difficulty[self.mode]

		if mode == "easy":
			self.width = 20
			self.height = 15
		elif mode == "normal":
			self.width = 25
			self.height = 15
		elif mode == "hard":
			self.width = 30
			self.height = 15
		
		self.CHECKED = [[0 for _ in range(self.width)] for _ in range(self.height)]
		self.field = [[0 for _ in range(self.width)] for _ in range(self.height)]