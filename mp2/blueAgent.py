from Gomoku import *

def blueWinningBlock(board):
	blocks = []
	for i in range(board.rows):
		for j in range(board.cols):
			currBlock = []
			if j + 4 < board.cols:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i][j+idx])
					idx += 1
				blocks.append(currBlock)

	for j in range(board.cols):
		for i in range(board.rows):
			currBlock = []
			if i + 4 < board.rows:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i+idx][j])
					idx += 1
				blocks.append(currBlock)

	for i in range(board.rows):
		for j in range(board.cols):
			currBlock = []
			if i+4 < board.rows and j+4 < board.cols:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i+idx][j+idx])
					idx += 1
				blocks.append(currBlock)

	for i in range(board.rows):
		for j in range(board.cols):
			currBlock = []
			if i-4 > 0 and j+4 > 0:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i-idx][j-idx])
					idx += 1
				blocks.append(currBlock)

	return blocks

def updateWinningBlocks_blue(blocks):
	for index, item in enumerate(blocks):
		for idx in item:
			if idx.isRed == True:
				blocks.pop[index]



