from Train import *

class Digits:
	def __init__(self):
		self.i = 0
		self.j = 0
		self.zero_prob = None
		self.total_digits = 0
		self.correctGuesses = 0
		self.totalGuesses = 0

		self.initializeProb()

	def initializeProb(self):
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

	def updateDigitProbs(self, num_array):
		self.total_digits += 1
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

	def division(self):
		k = 5
		a = 0
		while a < 32:
			b = 0
			zeroes = self.zero_prob[a]
			while b < 32:
				zeroes[b] = (zeroes[b] + k)/(self.total_digits + (k*2))
				b += 1
			a += 1
		#print(self.zero_prob)


