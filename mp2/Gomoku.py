from Node2 import *

class Board:
	def __init__(self):
		self.int_array = None
		self.node_array = None
		self.rows = -1
		self.cols = -1

		self.initialize()
		self.setNeighbors()

	def initialize(self):
		self.int_array = []
		i = 0
		while i < 7:
			emptyarray = []
			j = 0
			while j < 7:
				emptyarray.append(0) #0 for empty intersection
				j += 1
			self.int_array.append(emptyarray)
			i += 1
		print(self.int_array)

		self.rows = len(self.int_array)
		self.cols = len(self.int_array[0])

		self.node_array = []
		for i in range(self.rows):
			row = []	
			for j in range(self.cols):
				node = Node2(i, j, False, False)
				row.append(node)
			self.node_array.append(row)

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


