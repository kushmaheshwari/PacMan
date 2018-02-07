from Maze import *
from queue import *

def DFS():
	maze = Maze('mazes/mediumMaze.txt')	
	


	stack = []
	startingNode = maze.startingNode
	stack.append(startingNode)
	while len(stack) > 0:
		node = stack.pop()
		if node.isDot == True:
			#FOUND ENDING NODE. SEARCH COMPLETE
			print ("FOUND ENDING NODE DFS. SEARCH COMPLETE")
			break
		if node.visited == False:
			node.visited = True
			neighbors = node.neighbors
			for n in neighbors:
				if n.category != 0:
					stack.append(n)

def BFS():
	maze = Maze('mazes/mediumMaze.txt')
	
	
	queue = Queue(maxsize=0)
	startingNode = maze.startingNode
	queue.put(startingNode)
	while queue.qsize() > 0:
		node = queue.get()
		if node.isDot == True:
			#FOUND ENDING NODE. SEARCH COMPLETE
			print ("FOUND ENDING NODE BFS. SEARCH COMPLETE")
			break
		if node.visited == False:
			node.visited = True
			neighbors = node.neighbors
			for n in neighbors:
				if n.category != 0:
					queue.put(n)


if __name__ == "__main__":
    DFS()
    BFS()
