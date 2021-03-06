from math import log

class Test: #class that takes in and manipulates testing file
	def __init__(self, fname, train):

		self.num_array = None #array containing digit representation of test token
		self.map = None #array containing posterior probability of each digit class given a certain test token
		self.idx = None #max posterior probability from self.map

		self.fname = fname
		self.train = train
		self.matrix = None #holds counts of guessed vs actual class
		self.percentageMatrix = None #holds percentages of probabilities of matrix
		self.oddsMatrix = None #holds odd ratio matrix

		self.initializeMatrix()
		self.readTestFile()

	def readTestFile(self):
		self.num_array = []

		with open(self.fname) as f: #read in test file
		    	content = f.readlines()
		content = [x.strip() for x in content]
		
		counter = 0

		for line in content:
			row = []
			counter += 1
			for character in line:
				if (counter == 33): #looks at what class the image belongs (looks at digit)
					counter = 0
					self.calculatePosteriors(self.num_array)
					self.updateMax(self.idx, max(self.map), self.num_array)
					self.updateMin(self.idx, max(self.map), self.num_array)
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

		#print('Below is the class accuracy.')
		#print(self.train.classAccuracy)

		self.calcPercentages(self.matrix)

		self.printRatios()

		#c = 0
		#while c < 10:
		#	print(self.train.Digits[c].maxPost)
		#	self.printArray(self.train.Digits[c].maxNum_array)
		#	print(self.train.Digits[c].minPost)
		#	self.printArray(self.train.Digits[c].minNum_array)
		#	c += 1

	def calculatePosteriors(self, num_array): #calculates posterior probabilities
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

	def initializeMatrix(self): #initalizes confusion matrix
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


	def updateConfusion(self, num_array, character): #counts guessed digits given what digits it should actually be
		colIndex = int(character)
		rowIndex = self.idx
		intermed = self.matrix[rowIndex]
		intermed[colIndex] += 1

	def calcPercentages(self, matrix): #takes counts of guessed digits and calculates percentage that is correct
		self.percentageMatrix = []

		for row in matrix:
			line = []
			counter = 0
			for index, item in enumerate(row):
				dig = self.train.Digits[index]
				total = dig.totalGuesses
				value = item/total
				line.append('%.3f' % value)
			self.percentageMatrix.append(line)

		#print('Below is the confusion matrix.')
		#print(self.percentageMatrix)


	def printRatios(self): #print log of odd ratios and log of probabilities
		#actual - 2 vs guessed - 8
		#self.singularLog(7)
		self.oddsRatio(9, 7)


	def oddsRatio(self, digitOne, digitTwo): #print log of odd ratios
		self.oddsMatrix = []

		one = self.train.Digits[digitOne].one_prob
		two = self.train.Digits[digitTwo].one_prob

		for index, row in enumerate(one):
			line = []
			for idx, col in enumerate(row):
				currRow = two[index]
				currVal = currRow[idx]
				val = log(col/currVal)
				if (val > 1):
					value = '2'
				elif (val <= 1 and val > 0):
					value = '+'
				elif (val <= 0 and val > -1):
					value = '.'
				elif (val <= -1 and val >= -2):
					value = '-'
				else:
					value = '0'
				line.append(value)
			self.oddsMatrix.append(line)
		self.printArray(self.oddsMatrix)


	def singularLog(self, digit): #calculates feature likelihoods of a class
		one = self.train.Digits[digit].one_prob

		singLogMatrix = []

		for row in one:
			line = []
			for item in row:
				val = log(item)
				if (val > 0):
					value = '2'
				elif (val <= 0 and val > -0.5):
					value = '+'
				elif (val <= -0.5 and val > -1):
					value = '0'
				elif (val <= -1 and val >= -2.5):
					value = '-'
				else:
					value = '.'
				line.append(value)
			singLogMatrix.append(line)

		self.printArray(singLogMatrix)

	def updateMax(self, idx, val, num_array):
		obj = self.train.Digits[idx]
		if ((obj.maxPost == None) or (val > obj.maxPost)):
			obj.maxPost = val
			obj.maxNum_array = num_array

	def updateMin(self, idx, val, num_array):
		obj = self.train.Digits[idx]
		if ((obj.minPost == None) or (val < obj.minPost)):
			obj.minPost = val
			obj.minNum_array = num_array

	def printArray(self, array):
		for row in array:
			print(*row, sep='')






				