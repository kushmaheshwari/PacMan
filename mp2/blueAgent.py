from Gomoku import *

def blueWinningBlock(board):
	blocks = []
	myDict = defaultdict(list)
	for i in range(board.rows):
		for j in range(board.cols):
			currBlock = []
			if j + 4 < board.cols:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i][j+idx])
					idx += 1
				winBlock = winBlocks(currBlock, 'horizontal')
				idx = 0
				while idx < 5:
					l = j+idx
					string = str(i) + ", " + str(l)
					board.myDict[string].append(winBlock)
					idx += 1
				board.blocks.append(winBlock)


	for j in range(board.cols):
		for i in range(board.rows):
			currBlock = []
			if i + 4 < board.rows:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i+idx][j])
					idx += 1
				winBlock = winBlocks(currBlock, 'vertical')
				idx = 0
				while idx < 5:
					k = i+idx
					string = str(k) + ", " + str(j)
					board.myDict[string].append(winBlock)
					idx += 1
				board.blocks.append(winBlock)

	for i in range(board.rows):
		for j in range(board.cols):
			currBlock = []
			if i+4 < board.rows and j+4 < board.cols:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i+idx][j+idx])
					idx += 1
				winBlock = winBlocks(currBlock, 'incDiagonal')
				idx = 0
				while idx < 5:
					l = j+idx
					k = i+idx
					string = str(k) + ", " + str(l)
					board.myDict[string].append(winBlock)
					idx += 1
				board.blocks.append(winBlock)

	for i in range(board.rows):
		for j in range(board.cols):
			currBlock = []
			if i-4 >= 0 and j+4 < board.cols:
				idx = 0
				while idx < 5:
					currBlock.append(board.node_array[i-idx][j+idx])
					idx += 1
				winBlock = winBlocks(currBlock, 'decDiagonal')
				idx = 0
				while idx < 5:
					l = j+idx
					k = i-idx
					string = str(k) + ", " + str(l)
					board.myDict[string].append(winBlock)
					idx += 1
				board.blocks.append(winBlock)

def reflexAgentBlue(board):
	
	stones = []
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	spots = []
	for item in board.blocks:
		if (item.reds == 5 or item.blues == 5):
			board.victory = True
		if (item.state == 2 and item.blues == 4):
			stones[0].append(item)
		elif(item.state == 3 and item.reds == 4):
			stones[1].append(item)
		elif(item.state == 3 and item.reds == 3 and item.openEnded == 1):
			stones[2].append(item)
		elif (item.state == 2 and item.blues == 3):
			stones[3].append(item)
		elif (item.state == 2 and item.blues == 2):
			stones[4].append(item)
		elif (item.state == 2 and item.blues == 1):
			stones[5].append(item)
		else:
			stones[6].append(item)
	for m, item in enumerate(stones):
		if(item != []):
			for index in item:
				for idx in index.nodes:
					if (idx.isBlue == False and idx.isRed == False):
						if (m == 0 or m == 3 or m == 4 or m == 5) and (idx.isNeighbor() == 1 or idx.isNeighbor() == 2):
							spots.append(idx)
						elif (m == 1 or m == 2) and (idx.isNeighbor() == 1 or idx.isNeighbor() == 3):
							spots.append(idx)
			break
	i = 6 
	j = 6
	print (spots)
	if spots == [] and board.node_array[5][5].isBlue == False:
		board.updateBlocks2(5, 5, 1)
		#board.int_array[4][4] = 1
		return board
	for item in spots:
		if item.y <= j and item.x < i:
			j = item.y
			i = item.x
		if item.y < j:
			j = item.y
			i = item.x
	if (board.node_array[i][j].isBlue == False and board.node_array[i][j].isRed == False):
		board.updateBlocks2(i, j, 1)
	else:
		for i in range(board.rows):
			for j in range(board.rows):
				if (board.node_array[i][j].isBlue == False and board.node_array[i][j].isRed == False):
					board.updateBlocks2(i, j, 1)
					return board
	return board

def reflexAgentRed(board):
	
	stones = []
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	stones.append([])
	spots = []
	for item in board.blocks:
		if (item.reds == 5 or item.blues == 5):
			board.victory = True
		if (item.state == 3 and item.reds == 4):
			stones[0].append(item)
		elif(item.state == 2 and item.blues == 4):
			stones[1].append(item)
		elif(item.state == 2 and item.blues == 3 and item.openEnded == 1):
			stones[2].append(item)
		elif (item.state == 3 and item.reds == 3):
			stones[3].append(item)
		elif (item.state == 3 and item.reds == 2):
			stones[4].append(item)
		elif (item.state == 3 and item.reds == 1):
			stones[5].append(item)
	for m, item in enumerate(stones):
		if(item != []):
			for index in item:
				for idx in index.nodes:
					if (idx.isBlue == False and idx.isRed == False):
						if (m == 0 or m == 3 or m == 4 or m == 5) and (idx.isNeighbor() == 1 or idx.isNeighbor() == 3):
							spots.append(idx)
						elif (m == 1 or m == 2) and (idx.isNeighbor() == 1 or idx.isNeighbor() == 2):
							spots.append(idx)
			break
	i = 6 
	j = 6
	if spots == [] and board.node_array[1][1].isRed == False:
		board.updateBlocks2(1, 1, 2)
		#board.int_array[4][4] = 1
		return board
	for item in spots:
		if item.y <= j and item.x < i:
			j = item.y
			i = item.x
		if item.y < j:
			j = item.y
			i = item.x
	if (board.node_array[i][j].isRed == False and board.node_array[i][j].isBlue == False):
		board.updateBlocks2(i, j, 2)
	else:
		for i in range(board.rows):
			for j in range(board.rows):
				if (board.node_array[i][j].isRed == False and board.node_array[i][j].isBlue == False):
					board.updateBlocks2(i, j, 2)
					return board
	#board.int_array[i][j] = 1
	return board
