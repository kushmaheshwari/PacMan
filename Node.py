class Node:
	def __init__(self,category,isStarting,isDot):
		self.category = category
		self.visited = False
		self.neighbors = []
		self.isDot = isDot
