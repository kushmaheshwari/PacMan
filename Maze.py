class Maze:
	def __init__(self):
		self.num_array = None
		self.node_array = None
		self.cols = -1
		self.rows = -1

def readFile():
	self.num_array = []
	fname = 'medium maze path'
	with open(fname) as f:
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
	return self.num_array


def initialMaze():
    	readFile()
	self.node_array = []	

	for i in range(self.rows):
		row = []	
		for j in range(self.cols):
			node = None
			if self.num_array[i][j] == 0:
				node = Node(0,False)
			elif self.num_array[i][j] == 1:
				node = Node(1,False)
			elif self.num_array[i][j] == 2:
				node = Node (2,False)
			elif self.num_array[i][j] == 3:
				node = Node(3,False)
			row.append(node)
		self.node_array.append(row)


def updateNeighbors():
	for i in range(self.rows):
		for j in range(self.cols):
			node = self.node_array[i][j]
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


if __name__ == "__main__":
    main()














