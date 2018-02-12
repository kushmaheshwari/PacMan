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






def sortDots(dots, startingNode):
	dots.sort(key = lambda p: (abs(p.x - startingNode.x) + abs(p.y - startingNode.y)), reverse=True)
	return dots


def huersticAlgo():
	maze = Maze('mazes/ECMaze.txt')

	queue = []
	startingNode = maze.startingNode
	dots = sortDots(maze.dots,startingNode)
	endingNode = dots.pop()

	print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))


	startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
	startingNode.value = startingNode.h
	heappush(queue, (startingNode.value, startingNode))

	nodesExpanded = 0
	nodesVisitedTotal = 0
	pathCostTotal = 0
	
	while len(queue) > 0:
		newValue, node = heappop(queue)
		nodesExpanded += 1
		node.visited = True
		if node.isDot == True:
			print ("FOUND A Dot.")
			updatePathNodes(node)
			pathCost,nodesVisited = maze.printPath()
			pathCostTotal += pathCost
			nodesVisitedTotal += nodesVisited
			maze.clearVisited()
			queue = []
			node.isDot = False
			if len(dots) == 0:
				print ("FINISHED ALL DOTS.")
				updatePathNodes(node)
				pathCost,nodesVisited = maze.printPath()
				pathCostTotal += pathCost
				nodesVisitedTotal += nodesVisited
				break
			dots = sortDots(dots,node)
			endingNode = dots.pop()
			print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))
			startingNode = node
			startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
			startingNode.value = startingNode.h
			heappush(queue, (startingNode.value, startingNode))

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


	print ('Path Cost: ' + str(pathCostTotal))	
	print ('Nodes Visited: ' + str(nodesVisitedTotal))	
	print ('Nodes Expanded: ' + str(nodesExpanded))



def huersticAlgo2():
	maze = Maze('mazes/mediumSearch.txt')

	queue = []
	startingNode = maze.startingNode
	dots = sortDots(maze.dots,startingNode)
	endingNode = dots.pop()

	print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))


	startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
	startingNode.value = startingNode.h
	heappush(queue, (startingNode.value, startingNode))

	nodesExpanded = 0
	nodesVisitedTotal = 0
	pathCostTotal = 0



	vals = []
	for i in range(1,10):
		vals.append(str(i))
	for i in range(97,123):
		vals.append(chr(i))
	for i in range(65,91):
		vals.append(chr(i))

	vals.reverse()
	
	while len(queue) > 0:
		newValue, node = heappop(queue)
		nodesExpanded += 1
		node.visited = True

		if node.isDot == True:
			print ("FOUND A Dot.")
			updatePathNodes(node)
			pathCost,nodesVisited = maze.printPath()
			pathCostTotal += pathCost
			nodesVisitedTotal += nodesVisited
			maze.clearVisited()
			queue = []
			node.isDot = False
			node.printed = vals.pop()



			if len(dots) == 0:
				print ("FINISHED ALL DOTS.")
				updatePathNodes(node)
				pathCost,nodesVisited = maze.printPath()
				pathCostTotal += pathCost
				nodesVisitedTotal += nodesVisited
				break

			dots = sortDots(dots,node)
			endingNode = dots.pop()
			print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))
			startingNode = node
			startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
			startingNode.value = startingNode.h
			heappush(queue, (startingNode.value, startingNode))



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

		dots.append(endingNode)
		dots = sortDots(dots,node)
		endingNode = dots.pop()
		startingNode = node


	maze.printSolDots()
		# startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
		# startingNode.value = startingNode.h
		# heappush(queue, (startingNode.value, startingNode))


	print ('Path Cost: ' + str(pathCostTotal))	
	print ('Nodes Visited: ' + str(nodesVisitedTotal))	
	print ('Nodes Expanded: ' + str(nodesExpanded))


def ECBFS():
	maze = Maze('mazes/ECMaze.txt')

	queue = []
	startingNode = maze.startingNode
	dots = sortDots(maze.dots,startingNode)
	endingNode = dots.pop()

	print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))


	startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
	startingNode.value = startingNode.h
	heappush(queue, (startingNode.value, startingNode))

	nodesExpanded = 0
	nodesVisitedTotal = 0
	pathCostTotal = 0
	
	while len(queue) > 0:
		newValue, node = heappop(queue)
		nodesExpanded += 1
		node.visited = True
		if node.isDot == True:
			print ("FOUND A Dot.")
			updatePathNodes(node)
			pathCost,nodesVisited = maze.printPath()
			pathCostTotal += pathCost
			nodesVisitedTotal += nodesVisited
			maze.clearVisited()
			queue = []
			node.isDot = False
			if len(dots) == 0:
				print ("FINISHED ALL DOTS.")
				updatePathNodes(node)
				pathCost,nodesVisited = maze.printPath()
				pathCostTotal += pathCost
				nodesVisitedTotal += nodesVisited
				break
			dots = sortDots(dots,node)
			endingNode = dots.pop()
			print ('Ending Node: ' + str(endingNode.x) + ', ' + str(endingNode.y))
			startingNode = node
			startingNode.h = 10 * (abs(startingNode.x - endingNode.x) + abs(startingNode.y - endingNode.y))
			startingNode.value = startingNode.h
			heappush(queue, (startingNode.value, startingNode))

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


	print ('Path Cost: ' + str(pathCostTotal))	
	print ('Nodes Visited: ' + str(nodesVisitedTotal))	
	print ('Nodes Expanded: ' + str(nodesExpanded))




if __name__ == "__main__":
    DFS()
    # BFS()
    #Greedy()
    #AStar()
    # huersticAlgo()
    # huersticAlgo2()
