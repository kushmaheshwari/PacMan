from Maze import *
from queue import *
from heapq import *

def DFS():
	
	maze = Maze('mazes/mediumMaze.txt')	
	
	stack = [] #using a Stack for DFS
	startingNode = maze.startingNode
	stack.append(startingNode)
	while len(stack) > 0:
		node = stack.pop()
		node.visited = True
		if node.isDot == True: 
			print ("FOUND ENDING NODE DFS. SEARCH COMPLETE")
			updatePathNodes(node)
			maze.printPath()
			break
		neighbors = node.neighbors
		for n in neighbors:
			if n.category != 0 and n.visited == False: #add neighbors if not a Wall and not ever Visited
				n.parent = node #used to find the exact path
				stack.append(n)

def BFS():
	maze = Maze('mazes/mediumMaze.txt')
	
	
	queue = Queue(maxsize=0) #using a Queue for a BFS
	startingNode = maze.startingNode
	queue.put(startingNode)
	while queue.qsize() > 0:
		node = queue.get()
		if node.isDot == True:
			print ("FOUND ENDING NODE. SEARCH COMPLETE") #Search is complete so break out of the function
			updatePathNodes(node)
			maze.printPath()
			break
		node.visited = True
		neighbors = node.neighbors
		for n in neighbors:
			if n.category != 0 and n.visited == False: #add neighbors if not a Wall and not ever Visited
				n.visited = True
				n.parent = node #used to find the exact path
				queue.put(n)

def AStar():
	maze = Maze('mazes/mediumMaze.txt')

	queue = []
	startingNode = maze.startingNode
	endingNode = maze.endingNode
	startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y)) # h represents manhattan distance to ending node
	startingNode.value = startingNode.h
	heappush(queue, (startingNode.value, startingNode)) #using a Heap to determine what should be popped off the queue. 
	
	while len(queue) > 0:
		newValue, node = heappop(queue) #Node with the lowest value gets popped off. Value is h + g which is distance from start plus distance to end.
		node.visited = True
		if node.isDot == True:
			print ("FOUND ENDING NODE AStar. SEARCH COMPLETE")
			updatePathNodes(node)
			maze.printPath()
			break
		newG = node.g + 10 #g gets incremented by 10 
		neighbors = node.neighbors
		for n in neighbors:
			if n.visited == False or newG < n.g: 
				n.g = newG
				n.h = 10 * (abs(n.x - endingNode.x) + abs(n.y - endingNode.y)) # update the h value
				n.value = n.g + n.h #update the value to be the new g plus h
				if n.category != 0:
					n.parent = node
					heappush(queue, (n.value, n)) 




def Greedy():
    maze = Maze('mazes/mediumMaze.txt')

    queue = [] # queue for the algorithm

    startingNode = maze.startingNode
    endingNode = maze.endingNode
    startingNode.g = abs(startingNode.x - endingNode.x)
    startingNode.h = abs(startingNode.y - endingNode.y)
    startingNode.value = startingNode.g + startingNode.h
    heappush(queue, (startingNode.value, startingNode)) #using a heap to hold values
    

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
                n.g = abs(n.x - endingNode.x) #X manhattan distance to the end
                n.h = abs(n.y - endingNode.y) #Y manhattan distance to the end
                n.value = n.g + n.h #overall manhattan distance to the end
                if n.category != 0:
                    n.parent = node
                    heappush(queue, (n.value, n))

def updatePathNodes(Node): #update path nodes allows us to find the actual path
	node = Node
	while node.parent is not None:
		node.category = 2
		node = node.parent
	node.category = 2



def sortDots(dots, startingNode): #this sorts dots by distance to the node passed in
	dots.sort(key = lambda p: (abs(p.x - startingNode.x) + abs(p.y - startingNode.y)), reverse=True)
	return dots



def Astar2():
	maze = Maze('mazes/mediumSearch.txt')

	queue = []   #Queue holds all of the nodes
	startingNode = maze.startingNode
	dots = sortDots(maze.dots,startingNode)  #sorts the dot nodes based on manhattan distance to the starting node
	endingNode = dots.pop()  #picks the closest node based on manhattan distance and defines it as ending node

	print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))


	startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y)) #h is manhattan distance to closest dot
	startingNode.value = startingNode.h
	heappush(queue, (startingNode.value, startingNode)) 

	nodesExpanded = 0
	nodesVisitedTotal = 0
	pathCostTotal = 0

	vals = []  #creates a list from 1 - 9, a - z, A - Z for labeling the dots in order that they have been visisted
	for i in range(1,10):
		vals.append(str(i))
	for i in range(97,123):
		vals.append(chr(i))
	for i in range(65,91):
		vals.append(chr(i))

	vals.reverse()

	while len(queue) > 0: #While there are nodes
		newValue, node = heappop(queue)
		while (node.visited == True):  #Handles  duplicate nodes in the queue
			newValue, node = heappop(queue)
		nodesExpanded += 1 #Nodes expanded counter
		node.visited = True
		#print ('Current Node: ' + str(node.x) + ', ' + str(node.y) + ', ' + str(node.value))

		if node.isDot == True:
			print ("FOUND A Dot.")
			updatePathNodes(node)  #Used for printing and counting the correct path and debugging
			pathCost,nodesVisited = maze.printPath() 
			nodesExpanded -= 1
			print ('Nodes Expanded: ' + str(nodesExpanded))

			pathCostTotal += pathCost
			nodesVisitedTotal += nodesVisited
			maze.clearVisited()  #Clear visited nodes
			queue = [] #Clears queue
			node.isDot = False #Sets the dot to false
			node.printed = vals.pop() #orders dots

			if len(dots) == 0: #if dot list length is zero, break loop
				print ("FINISHED ALL DOTS.")
				updatePathNodes(node)
				pathCost,nodesVisited = maze.printPath()
				pathCostTotal += pathCost
				nodesVisitedTotal += nodesVisited
				break

			dots = sortDots(dots,node) #Resort the remaining dots
			endingNode = dots.pop()
			print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))
			startingNode = node #reestablishes the starting node
			startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y)) #manhattan distance
			startingNode.value = startingNode.h
			heappush(queue, (startingNode.value, startingNode)) 

		dots.append(endingNode) #adds the ending node so it can be sorted again
		dots = sortDots(dots,node) #sorts dots again just incase there is another closer dot to the current node
		endingNode = dots.pop()
		startingNode = node

		newG = node.g + 10 #g is the calculated steps from the beginning. every new node adds 10 more.
		neighbors = node.neighbors #finds neighbors
		for n in neighbors:
			if n.visited == False or newG < n.g: #if neighbors have not been visited or there is a shorter path to the neighbor
				n.g = newG #set new g
				n.h = 10 * (abs(n.x - endingNode.x) + abs(n.y - endingNode.y)) #set manhattan distance to closest dot
				n.value = n.g + n.h #adds g and h
				if n.category != 0: # if not a wall
					n.parent = node
					heappush(queue, (n.value, n)) #heap automatically sorts the queue based on the value

		
	maze.printSolDots() #print maze with ordered dots

	print ('Path Cost: ' + str(pathCostTotal))	
	print ('Nodes Visited: ' + str(nodesVisitedTotal))	
	print ('Nodes Expanded: ' + str(nodesExpanded))






if __name__ == "__main__":
    DFS()
    BFS()
    Greedy()
    AStar()
    Astar2()
