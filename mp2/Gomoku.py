from Node2 import *
from winBlocks import *
from collections import defaultdict

class Board:
	def __init__(self):
		self.int_array = None
		self.node_array = None
		self.rows = -1
		self.cols = -1

		self.blocks = []
		self.myDict = defaultdict(list)

		self.victory = False

		self.initialize()
		self.printNodes()
		self.setNeighbors()

	def initialize(self):
		self.int_array = []
	
		emptyarray1 = [0, 0, 0, 0, 0, 0, 0]
		emptyarray2 = [0, 0, 0, 0, 0, 0, 0]
		emptyarray3 = [0, 0, 0, 0, 0, 0, 0]
		emptyarray4 = [0, 0, 0, 0, 0, 0, 0]
		emptyarray5 = [0, 0, 0, 0, 0, 0, 0]
		emptyarray6 = [0, 0, 0, 0, 0, 0, 0]
		emptyarray7 = [0, 0, 0, 0, 0, 0, 0]

		self.int_array.append(emptyarray7)
		self.int_array.append(emptyarray6)
		self.int_array.append(emptyarray5)
		self.int_array.append(emptyarray4)
		self.int_array.append(emptyarray3)
		self.int_array.append(emptyarray2)
		self.int_array.append(emptyarray1)

		self.rows = len(self.int_array)
		self.cols = len(self.int_array[0])

		self.node_array = []
		for i in range(self.rows):
			row = []	
			for j in range(self.cols):
				if (self.int_array[i][j] == 0):
					node = Node2(i, j, False, False)
				elif (self.int_array[i][j] == 1):
					node = Node2(i, j, True, False)
				elif (self.int_array[i][j] == 2):
					node = Node2(i, j, False, True)	
				row.append(node)
			self.node_array.append(row)

	def printNodes(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if (self.node_array[i][j].isBlue):
					self.int_array[6-i][j] = '1'
				elif (self.node_array[i][j].isRed):
					self.int_array[6-i][j] = '2'
				else:
					self.int_array[6-i][j] = '.'
		for i in range(self.rows):
			print(self.int_array[i])
		print('----------------------------------------------------')

	def setNeighbors(self):
		for i in range(self.rows):
			for j in range(self.cols):
				neighbors = []
				if i-1 > 0:
					neighbors.append(self.node_array[i-1][j])			
				if i+1 < self.rows:
					neighbors.append(self.node_array[i+1][j])			
				if j-1 > 0:
					neighbors.append(self.node_array[i][j-1])			
				if j+1 < self.cols:
					neighbors.append(self.node_array[i][j+1])
				if (i-1 > 0) and (j-1 > 0):
					neighbors.append(self.node_array[i-1][j-1])
				if (i+1 < self.rows) and (j-1 > 0):
					neighbors.append(self.node_array[i+1][j-1])	
				if (i-1 > 0) and (j+1 < self.cols):
					neighbors.append(self.node_array[i-1][j+1])	
				if (i+1 < self.rows) and (j+1 < self.cols):
					neighbors.append(self.node_array[i+1][j+1])			
				self.node_array[i][j].neighbors = neighbors

	def updateBlocks(self, i, j, color):
		string = str(i) + ", " + str(j)
		changeBlocks = self.myDict[string]
		node = self.node_array[i][j]
		if color == 1:
			node.isBlue = True
		elif color == 2:
			node.isRed = True
		else:
			node.isBlue = False
			node.isRed = False
		for item in changeBlocks:
			item.updateBlock()

