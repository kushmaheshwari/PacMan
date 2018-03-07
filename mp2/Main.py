from smartManufacturing import *
from queue import *

def partOne():
	data = smartManufacturing()
	print(data.widgets[0])

	letterA = 0
	letterB = 0
	letterC = 0
	letterD = 0
	letterE = 0

	for item in data.widgets:
		character = item.get()
		if (character == 'A'):
			letterA += 1
		if (character == 'B'):
			letterB += 1
		if (character == 'C'):
			letterC += 1
		if (character == 'D'):
			letterD += 1
		if (character == 'E'):
			letterE += 1

	print("A = " + str(letterA) + ", B = " + str(letterB) + ", C = " + str(letterC) + ", D = " + str(letterD) + ", E = " + str(letterE))


if __name__ == "__main__":
	partOne()	
