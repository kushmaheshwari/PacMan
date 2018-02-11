from Maze import *
from queue import *
from heapq import *

def DFS():
	maze = Maze('mazes/mediumMaze.txt')	
	


	stack = []
	startingNode = maze.startingNode
	stack.append(startingNode)
	while len(stack) > 0:
		node = stack.pop()
		node.visited = True
		if node.isDot == True:
			#FOUND ENDING NODE. SEARCH COMPLETE
			print ("FOUND ENDING NODE DFS. SEARCH COMPLETE")
			updatePathNodes(node)
			maze.printPath()
			break
		neighbors = node.neighbors
		for n in neighbors:
			if n.category != 0 and n.visited == False:
				n.parent = node
				stack.append(n)

def BFS():
	maze = Maze('mazes/tinySearch.txt')
	
	
	queue = Queue(maxsize=0)
	startingNode = maze.startingNode
	queue.put(startingNode)
	while queue.qsize() > 0:
		node = queue.get()
		if node.isDot == True:
			#FOUND ENDING NODE. SEARCH COMPLETE
			print (" ")
			updatePathNodes(node)
			maze.printPath()
			maze.clearVisited()
			queue.queue.clear()
			node.isDot = False
			maze.dots.remove(node)
		if len(maze.dots) == 0:
			print ("FOUND ENDING NODE BFS. SEARCH COMPLETE")
			break
		node.visited = True
		neighbors = node.neighbors
		for n in neighbors:
			if n.category != 0 and n.visited == False:
				n.visited = True
				n.parent = node
				queue.put(n)

def AStar():
	maze = Maze('mazes/mediumMaze.txt')

	queue = []
	startingNode = maze.startingNode
	endingNode = maze.endingNode
	startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
	startingNode.value = startingNode.h
	heappush(queue, (startingNode.value, startingNode))
	
	while len(queue) > 0:
		newValue, node = heappop(queue)
		node.visited = True
		if node.isDot == True:
			print ("FOUND ENDING NODE AStar. SEARCH COMPLETE")
			updatePathNodes(node)
			maze.printPath()
			break
		newG = node.g + 10
		neighbors = node.neighbors
		for n in neighbors:
			if n.visited == False or newG < n.g:
				n.g = newG
				n.h = 10 * (abs(n.x - endingNode.x) + abs(n.y - endingNode.y))
				n.value = n.g + n.h
				if n.category != 0:
					n.parent = node
					heappush(queue, (n.value, n))

def Greedy():
    maze = Maze('mazes/mediumMaze.txt')

    queue = []
    startingNode = maze.startingNode
    endingNode = maze.endingNode
    startingNode.g = abs(startingNode.x - endingNode.x)
    startingNode.h = abs(startingNode.y - endingNode.y)
    startingNode.value = startingNode.g + startingNode.h
    heappush(queue, (startingNode.value, startingNode))
    

    while len(queue) > 0:
        newValue, node = heappop(queue)
        node.visited = True
        if node.isDot == True:
            print ("FOUND ENDING NODE GREEDY. SEARCH COMPLETE")
            updatePathNodes(node)
            maze.printPath()
            break
        neighbors = node.neighbors
        for n in neighbors:
            if n.visited == False:
                n.g = abs(n.x - endingNode.x)
                n.h = abs(n.y - endingNode.y)
                n.value = n.g + n.h
                if n.category != 0:
                    n.parent = node
                    heappush(queue, (n.value, n))

def updatePathNodes(Node):
	node = Node
	while node.parent is not None:
		node.category = 2
		node = node.parent
	node.category = 2

#def huersticAlgo(Node):


if __name__ == "__main__":
    #DFS()
    BFS()
    #Greedy()
    #AStar()
