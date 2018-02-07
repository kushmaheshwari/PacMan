from Maze import *
from queue import *

def DFS():
	maze = Maze('mazes/mediumMaze.txt')	
	

	stack = []
	startingNode = maze.startingNode
	stack.append(startingNode)
	while len(stack) != 0:
		node = stack.pop()
		if node.isDot == True:
			#FOUND ENDING NODE. SEARCH COMPLETE
		if node.visited == False:
			node.visisted = True
			neighbors = node.neighbors
			for n in neighbors:
				if n.category != 0:
					stack.append(n)

def BFS():
	maze = Maze('mazes/mdeiumMaze.txt')
	
	
	queue = Queue(maxsize=0)
	startingNode = maze.StartingNode
	queue.put(startingNode)
	while len(queue) != 0:
		node = queue.get()
		if node.isDot == True:
			#FOUND ENDING NODE. SEARCH COMPLETE
		if node.visisted == False:
			node.visisted = True
			neighbors = node.neighbors
			for n in neighbors:
				if n.category != 0:
					queue.put(n)



