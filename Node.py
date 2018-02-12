class Node:
	def __init__(self,x, y, category,isStarting,isDot):
		self.category = category
		self.visited = False
		self.neighbors = []
		self.isDot = isDot
		self.g = 0
		self.h = 0
		self.value = 0
		self.x = x
		self.y = y
		self.parent = None
		self.printed = -1

	def __lt__(self, other):
		if (self.value < other.value):
			return self
		return other
