from Gomoku import *

class winBlocks:
	def __init__(self, nodes, orientation):
		self.nodes = nodes
		self.blues = 0
		self.reds = 0
		self.state = 0  #0 empty, 1 both, 2 blue, 3 red
		self.orientation = orientation

		self.updateBlock()

	def updateBlock(self):
		self.blues = 0
		self.reds = 0
		for item in self.nodes:
			if (item.isBlue):
				self.blues += 1
			if (item.isRed):
				self.reds += 1
		if (self.blues > 0 and self.reds > 0):
			self.state = 1
		elif(self.blues > 0):
			self.state = 2
		elif(self.reds > 0):
			self.state = 3