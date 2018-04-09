from Train import *
import random
import decimal

class Digits: #class that contains information about each digit class
	def __init__(self):

		self.zero_prob = None #32x32 array containing probability that each pixel is a 0 given the class
		self.total_digits = 0 #total count of input images
		self.correctGuesses = 0 #number of guesses about class that are correct
		self.totalGuesses = 0 #total number of guesses (whether right or wrong)
		self.one_prob = None #32x32 array containing probability that each pixel is a 1 given the class
		self.maxNum_array = None #test token with highest posterior probability
		self.maxPost = None #highest posterior probability
		self.minNum_array = None #test token with lowest posterior probability
		self.minPost = None #lowest posterior probability

		self.weights = None
		self.bias = 0

		self.initializeProb()
		self.initializeWeights()
		self.initializeMax()
		self.initializeMin()

	def initializeProb(self): #creates empty 32x32 array to hold probability of 0 for each pixel
		self.zero_prob = []

		a = 0
		while a < 32:
			b = 0
			row = []
			while b < 32:
				row.append(0)
				b += 1
			self.zero_prob.append(row)
			a += 1

	def updateDigitProbs(self, num_array): #update count of how many times a zero shows up at a certain pixel given a class
		self.total_digits += 1 #keep count of input instances
		a = 0
		while a < 32:
			b = 0
			while b < 32:
				zeroes = self.zero_prob[a]
				intermed = num_array[a]
				if (intermed[b] == 0):
					zeroes[b] += 1
				b += 1
			a += 1


	def division(self): #divide the count of zeroes in zero_prob to calcuate percentage
		k = 6 #most ideal constant for laplace smoothing
		a = 0
		while a < 32:
			b = 0
			zeroes = self.zero_prob[a]
			while b < 32:
				zeroes[b] = (zeroes[b] + k)/(self.total_digits + (k*2))
				b += 1
			a += 1
		#print(self.zero_prob)

	def convertToOne(self): #convert zero_prob to calculate probability of 1
		self.one_prob = []

		for row in self.zero_prob:
			line = []
			for item in row:
				value = 1 - item
				line.append(value)
			self.one_prob.append(line)

	def initializeWeights(self):
		self.weights = []
		x = 0

		a = 0
		while a < 32:
			b = 0
			row = []
			while b < 32:
				#x = float(decimal.Decimal(random.randrange(-99, 99))/100)
				row.append(x)
				b += 1
			self.weights.append(row)
			a += 1

	def initializeMax(self): #initializes num_array for test token with maximum posterior probability for the digit class
		self.maxNum_array = []

		a = 0
		while a < 32:
			b = 0
			row = []
			while b < 32:
				row.append(0)
				b += 1
			self.maxNum_array.append(row)
			a += 1
	

	def updateWeights(self, lRate, Error, num_array):
		self.bias = self.bias + lRate*Error

		a = 0
		while a < 32:
			b = 0
			row = self.weights[a]
			numRow = num_array[a]
			while b < 32:
				row[b] = row[b] + lRate*Error*numRow[b]
				b += 1

	def initializeMin(self): #initializes num_array for test token with minimum posterior probability for the digit class
		self.minNum_array = []

		a = 0
		while a < 32:
			b = 0
			row = []
			while b < 32:
				row.append(0)
				b += 1
			self.minNum_array.append(row)
			a += 1

