from math import log
from decimal import Decimal

class Test:
	def __init__(self, fname, train):
		stringGuess = ""
		self.num_array = None
		self.map = None
		self.idx = None
		self.fname = fname
		self.train = train
		self.matrix = None
		self.percentageMatrix = None

		self.initializeMatrix()
		self.readTestFile()

	def readTestFile(self):
		self.num_array = []

		with open(self.fname) as f:
		    	content = f.readlines()
		content = [x.strip() for x in content]
		
		counter = 0

		for line in content:
			row = []
			counter += 1
			for character in line:
				if (counter == 33):
					counter = 0
					self.calculatePosteriors(self.num_array)
					self.num_array = []
					digit = self.train.Digits[int(character)]
					digit.totalGuesses += 1
					if (self.idx == int(character)):
						#print('True')
						digit.correctGuesses += 1
					#print(digit.correctGuesses/digit.totalGuesses)	
					self.updateConfusion(self.num_array, character)						
				else:
					row.append(int(character))
			if (counter != 0):
				self.num_array.append(row)

		cc = 0
		while cc < 10:
			digital = self.train.Digits[cc]
			self.train.classAccuracy.append(digital.correctGuesses/digital.totalGuesses)
			cc += 1

		print('Below is the class accuracy.')
		print(self.train.classAccuracy)

		self.calcPercentages(self.matrix)

	def calculatePosteriors(self, num_array):
		self.map = []

		total = 0

		c = 0
		while c < 10:
			digit = self.train.Digits[c]

			total = 0

			total += log(self.train.priors[c])

			a = 0
			while a < 32:
				b = 0
				while b < 32:
					zeroes = digit.zero_prob[a]
					intermed = num_array[a]
					if (intermed[b] == 0):
						total += log(zeroes[b])
					else:
						total += log(1 - zeroes[b])
					b += 1
				a += 1

			self.map.append(total)
			c += 1
		#print('-------------------------------------------------------')
		#print(self.map)
		self.idx = self.map.index(max(self.map))
		#print(self.idx)

	def initializeMatrix(self):
		self.matrix = []

		a = 0
		while a < 10:
			row = []
			b = 0
			while b < 10:
				row.append(0)
				b += 1
			self.matrix.append(row)
			a += 1


	def updateConfusion(self, num_array, character):
		colIndex = int(character)
		rowIndex = self.idx
		intermed = self.matrix[rowIndex]
		intermed[colIndex] += 1

	def calcPercentages(self, matrix):
		self.percentageMatrix = []

		for row in matrix:
			line = []
			counter = 0
			for index, item in enumerate(row):
				dig = self.train.Digits[index]
				total = dig.totalGuesses
				line.append(item/total)
			self.percentageMatrix.append(line)

		print('Below is the confusion matrix.')
		print(self.percentageMatrix)






				