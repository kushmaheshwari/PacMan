from Digits import * 
from Test import *

class Train:
	def __init__(self, fname):
		self.num_array = None
		self.num_digits = None
		self.curDigit = None
		self.priors = None
		self.Digits = None

		self.fname = fname

		self.readFile()
		self.calcPriors()

	def readFile(self):
		self.num_array = []
		self.num_digits = []
		self.Digits = []

		a = 0
		while (a < 10):
			digit = Digits()
			self.num_digits.append(0)
			self.Digits.append(digit)
			a += 1

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
					self.num_digits[int(character)] += 1
					self.curDigit = int(character)
					self.Digits[int(character)].updateDigitProbs(self.num_array)
					self.num_array = []
				else:
					row.append(int(character))
			if (counter != 0):
				self.num_array.append(row)
		cc = 0
		while cc < 10:
			print ("--------------------------------------------------------------------------------------------")
			self.Digits[cc].division()
			cc += 1

	def calcPriors(self):
		self.priors = []

		total = 0
		for val in self.num_digits:
			total = total + val

		for val in self.num_digits:
			prob = val/total
			self.priors.append(prob)

		print(self.priors)

if __name__ == "__main__":
	train = Train('digitdata/digitdata/optdigits-orig_train.txt')
	test = Test('digitdata/digitdata/optdigits-orig_test.txt', train)
	print (train.num_digits)
