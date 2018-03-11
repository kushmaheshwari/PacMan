from smartManufacturing import *
from queue import *
from Node import *
from heapq import *
from Gomoku import *
from blueAgent import *

def partOne():
	data = smartManufacturing()
	counter = 0
	countLetters(data)
	printLetterCount(data)

	queue = []

	updateQueue(data, queue, '')

	while (len(queue) > 0):
		counter += 1
		value, node = heappop(queue)
		phrase = node.phrase
		phrase += node.letter
		print(phrase, node.value)
		countLetters(data)
		#printLetterCount(data)

		data = smartManufacturing()

		popQueues(data, phrase)
		countLetters(data)
		updateQueue(data, queue, phrase)
		printLetterCount(data)
		
		
		if (data.totalLetters == 0):
			print ("Finished = " + phrase + ', Value = ' + str(node.value) + ', nodes expanded = ' + str(counter))
			#print("Length = " + len(phrase))
			break
		#if counter == 8:
		#	break



	#while(letterA != 0 && letterB != 0 && letterC != 0 && letterD != 0 && letterE != 0)

def countLetters(data):
	for item in data.widgets:
		if len(item) != 0:
			character = item[0]
			if (character == 'A'):
				data.letters[0] += 1
			if (character == 'B'):
				data.letters[1] += 1
			if (character == 'C'):
				data.letters[2] += 1
			if (character == 'D'):
				data.letters[3] += 1
			if (character == 'E'):
				data.letters[4] += 1

	data.totalLetters = data.letters[0] + data.letters[1] + data.letters[2] + data.letters[3] + data.letters[4]

def printLetterCount(data):
	print("A = `" + str(data.letters[0]) + ", B = " + str(data.letters[1]) + ", C = " + str(data.letters[2]) + ", D = " + str(data.letters[3]) + ", E = " + str(data.letters[4]))
	print('total = ' + str(data.totalLetters))

def maxWidgetLength(data):
	return max(len(data.widgets[0]), len(data.widgets[1]), len(data.widgets[2]), len(data.widgets[3]), len(data.widgets[4]))

def maxLetter(data):
	#return max(data.letters[0], data.letters[1], data.letters[2], data.letters[3], data.letters[4])
	return max(data.letters)

def popQueues(data, str):
	for i in str:
		for item in data.widgets:
			if len(item) != 0:
				if item[0] == i:
					character = item.pop(0)

def updateQueue(data, queue, phrase):
	for index, item in enumerate(data.letters):
		#if (maxLetter(data) == 0):
		#	print('break')
		#	break
		if (item != 0):
			value = maxWidgetLength(data) + maxLetter(data) - item + len(phrase)
			#value = maxWidgetLength(data) + len(phrase) 
			print (index, maxWidgetLength(data), maxLetter(data), item, len(phrase))
			if (index == 0):
				#print('amount = ' + str(item) + ', value = ' + str(value) + ', letter = A')
				node = Node('A', value, 5, phrase)
				heappush(queue, (node.value, node))
			if (index == 1):
				#print('amount = ' + str(item) + ', value = ' + str(value) + ', letter = B')
				node = Node('B', value, 5, phrase)
				heappush(queue, (node.value, node))
			if (index == 2):
				#print('amount = ' + str(item) + ', value = ' + str(value) + ', letter = C')
				node = Node('C', value, 5, phrase)
				heappush(queue, (node.value, node))
			if (index == 3):
				#print('amount = ' + str(item) + ', value = ' + str(value) + ', letter = D')
				node = Node('D', value, 5, phrase)
				heappush(queue, (node.value, node))
			if (index == 4):
				#print('amount = ' + str(item) + ', value = ' + str(value) + ', letter = E')
				node = Node('E', value, 5, phrase)
				heappush(queue, (node.value, node))

def partTwo():
	data = smartManufacturing()

	counter = 0
	countLetters2(data)
	printLetterCount(data)
	print(data.maxHeuristic)

	queue = []

	updateQueue2(data, queue, '', 0)

	while (len(queue) > 0):
		counter += 1
		value, node = heappop(queue)
		print(node.letter)
		phrase = node.phrase
		phrase += node.letter
		print(phrase, node.h)
		countLetters2(data)
		printLetterCount(data)

		data = smartManufacturing()

		popQueues(data, phrase)
		countLetters2(data)
		updateQueue2(data, queue, phrase, node.h)
		printLetterCount(data)

		if (data.totalLetters == 0):
			print ("Finished = " + phrase)
			print("Length = " + str(len(phrase)))
			print('Miles = ' + str(node.value) + ', nodes expanded = ' + str(counter))
			break

def updateQueue2(data, queue, phrase, distToState):
	for index, item in enumerate(data.letters):
		if item != 0:
			if (phrase == ''):
				dist = 0
			else:
				dist = data.distances[index]
				if (phrase[-1:] == 'A'):
					dist = dist[0]
				if (phrase[-1:] == 'B'):
					dist = dist[1]
				if (phrase[-1:] == 'C'):
					dist = dist[2]
				if (phrase[-1:] == 'D'):
					dist = dist[3]
				if (phrase[-1:] == 'E'):
					dist = dist[4]

			#value = max(data.maxHeuristic) + (dist * (maxLetter(data) - item + 1)) + distToState
			value = max(data.maxHeuristic) + dist + distToState
			
			print(value)
			if index == 0:
				node = Node('A', value, dist + distToState, phrase)
				heappush(queue, (node.value, node))
			if index == 1:
				node = Node('B', value, dist + distToState, phrase)
				heappush(queue, (node.value, node))
			if index == 2:
				node = Node('C', value, dist + distToState, phrase)
				heappush(queue, (node.value, node))
			if index == 3:
				node = Node('D', value, dist + distToState, phrase)
				heappush(queue, (node.value, node))
			if index == 4:
				node = Node('E', value, dist + distToState, phrase)
				heappush(queue, (node.value, node))


def countLetters2(data):
	for index, item in enumerate(data.widgets):
		if len(item) != 0:
			character = item[0]
			length = len(item)
			value = data.heuristics[index]
			value = value[5-length]
			if (character == 'A'):
				letNum = 0
			if (character == 'B'):
				letNum = 1
			if (character == 'C'):
				letNum = 2
			if (character == 'D'):
				letNum = 3
			if (character == 'E'):
				letNum = 4

			data.letters[letNum] += 1
			if (value > data.maxHeuristic[letNum]):
				data.maxHeuristic[letNum] = value

	data.totalLetters = data.letters[0] + data.letters[1] + data.letters[2] + data.letters[3] + data.letters[4]

if __name__ == "__main__":
    data = smartManufacturing()
    #partOne()
    #partTwo()
    board = Board()
    blocks = blueWinningBlock(board)
    updateWinningBlocks_blue(blocks)
