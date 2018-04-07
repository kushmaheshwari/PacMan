from math import log

class Test:
	def __init__(self, fname, train):
		stringGuess = ""
		self.num_array = None
		self.map = None
		self.idx = None
		self.fname = fname
		self.train = train

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
						print('True')
						digit.correctGuesses += 1
					print(digit.correctGuesses/digit.totalGuesses)							
				else:
					row.append(int(character))
			if (counter != 0):
				self.num_array.append(row)

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
		print('-------------------------------------------------------')
		print(self.map)
		self.idx = self.map.index(max(self.map))
		print(self.idx)

		