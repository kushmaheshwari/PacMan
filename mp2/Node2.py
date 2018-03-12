class Node2:
	def __init__(self, x, y, isBlue, isRed):
		self.x = x
		self.y = y
		self.isBlue = isBlue
		self.isRed = isRed
		self.neighbors = []
		self.neighbor = self.isNeighbor() #0 is no neighbors, 1 is both red and blue neighbors, 2 is blue, 3 is red
		self.letter = ''

	def isNeighbor(self):
		i = 0
		j = 0
		for item in self.neighbors:
			if item.isBlue == True:
				i = 1
			if item.isRed == True:
				j = 1
		if i > 0 and j > 0:
			return 1
		elif i > 0:
			return 2
		elif j > 0:
			return 3
		return 0

