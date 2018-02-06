class ReadFile:
	def __init__(self):
		self.array = None
		self.cols = -1
		self.rows = -1

def readFile():

	maze = ReadFile()

	maze.array = []
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
		maze.array.append(row)
		

if __name__ == "__main__":
    main()






















