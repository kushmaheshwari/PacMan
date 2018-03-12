from Gomoku import *
from copy import deepcopy

def searchTree(board, depth):
	if depth == 3:
		weight = weighBoard(board)
		return board, weight
	newboard = board
	x = 8
	y = 8
	if depth == 1:
		value = 1000
	else:
		value = -1000
	for i in range(board.rows):
		for j in range(board.cols):
			if (board.node_array[i][j].isBlue == False and board.node_array[i][j].isRed == False):
				if depth == 1:
					newboard.updateBlocks(i, j, 1)
					updatedboard, weight = searchTree(newboard, depth + 1)
					newboard.updateBlocks(i, j, 0)
					if (weight < value):
						value = weight
						x = i
						y = j
				else:
					newboard.updateBlocks(i, j, 2)
					updatedboard, weight = searchTree(newboard, depth + 1)
					newboard.updateBlocks(i, j, 0)
					#print (depth, value, weight, x, y)
					#updatedboard.printNodes()
					if (weight > value):
						value = weight
						x = i
						y = j
						#print (depth, value, weight, x, y)

	#print(depth, x)
	if depth == 0 and x != 8:
		newboard.updateBlocks2(x, y, 2)
	return newboard, value

def weighBoard(board):
	weight = 0

	for item in board.blocks:
		if (item.state == 2 and item.blues == 5):
			weight -= 200
		elif (item.state == 2 and item.blues == 4):
			weight -= 51
		elif (item.state == 2 and item.blues == 3 and item.openEnded == 1):
			weight -= 51
		elif (item.state == 2 and item.blues == 3):
			weight -= 26
		elif (item.state == 2 and item.blues == 2):
			weight -= 13
		#elif (item.state == 2 and item.blues == 1):
		#	stones[4].append(item)
		#elif(item.state == 3 and item.reds == 1):
		#	stones[5].append(item)
		elif(item.state == 3 and item.reds == 2):
			weight += 13
		elif(item.state == 3 and item.reds == 3):
			weight +=26
		elif (item.state == 3 and item.blues == 3 and item.openEnded == 1):
			weight += 51
		elif(item.state == 3 and item.reds == 4):
			weight += 51
		elif(item.state == 3 and item.reds == 5):	
			weight += 200	

	return weight