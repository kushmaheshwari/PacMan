from Node import *

class Maze:
	def __init__(self,fname):
		self.num_array = None
		self.node_array = None
		self.cols = -1
		self.rows = -1
		self.fname = fname
		self.startingNode = None
		self.endingNode = None
		self.dots = []

		self.readFile()
		self.initializeMaze()
		self.updateNeighbors()
		


	def readFile(self):
		self.num_array = []
		with open(self.fname) as f:
		    	content = f.readlines()
		content = [x.strip() for x in content]

		#read each line
		for line in content:
			row = []
			for character in line:
				if character == '%': #0 for wall
					row.append(0)
				elif character == ' ': #1 for space
					row.append(1)
				elif character == 'P': #2 for starting
					row.append(2)
				elif character == '.': #3 for dot
					row.append(3)
			self.num_array.append(row)
		


		self.rows = len(content)
		self.cols = len(content[0]) 

	def initializeMaze(self):
		self.node_array = []	

		for i in range(self.rows):
			row = []	
			for j in range(self.cols):
				node = None
				if self.num_array[i][j] == 0:
					node = Node(i, j, 0,False,False)
				elif self.num_array[i][j] == 1:
					node = Node(i, j, 1,False,False)
				elif self.num_array[i][j] == 2:
					node = Node (i, j, 2,True,False)
					self.startingNode = node
				elif self.num_array[i][j] == 3:
					node = Node(i, j, 3,False,True)
					self.endingNode = node
					self.dots.append(node)
				row.append(node)
			self.node_array.append(row)


	def updateNeighbors(self):
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
				self.node_array[i][j].neighbors = neighbors 

	def printMaze(self):
		for i in range(self.rows):
			for j in range(self.cols):
				print(self.num_array[i][j], end='')
			print ()

	def printPath(self):
		pathCost = 0
		nodesVisited = 0

		for i in range(self.rows):
			for j in range(self.cols):
				if self.node_array[i][j].category == 2:
					print(".", end='')
					pathCost += 1
				elif self.node_array[i][j].category == 0:
					print("X", end='')
				elif self.node_array[i][j].visited:
					print("1", end='')
					nodesVisited += 1
				else:
					print(" ", end='')
			print ()

		pathCost -= 1 #take out starting and ending node
		nodesVisited += pathCost #adding the path plus any 1s to get all nodes visited. PathCost is just nodes in the path

		print ('Path Cost: ' + str(pathCost))
		print ('Nodes Visted: ' + str(nodesVisited))
		print ('=======================================')
		return pathCost,nodesVisited

	def clearVisited(self):
		for i in range(self.rows):
			for j in range(self.cols):
				self.node_array[i][j].visited = False
				self.node_array[i][j].parent = None	
				if self.node_array[i][j].category == 2:
					self.node_array[i][j].category = 1		

