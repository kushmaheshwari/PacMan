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

def Greedy():
    maze = Maze('mazes/mediumMaze.txt')

    queue = []
    startingNode = maze.startingNode
    endingNode = maze.endingNode
    queue.put(startingNode)
    
    while len(queue) > 0:
        node = queue.get()
        if node.isDot == True:
            print ("FOUND ENDING NODE GREEDY. SEARCH COMPLETE")
            updatePathNodes(node)
            maze.printPath()
            break
        if node.visited == False:
            node.visited = True
            neighbors = node.neighbors
            diff = {}
            for n in neighbors:
                n.g = abs(n.x - endingNode.x)
                n.h = abs(n.y - endingNode.y)
                n.value = n.g + n.h
                if n.category != 0:
                    n.parent = node
                    diff[n.value] = n
            while len(diff) > 0:
                minKey = min(k for k, v in diff.iteritems())
                queue.put(diff[minKey])
                diff.pop(minKey)



if __name__ == "__main__":
    DFS()
    BFS()
    Greedy()
