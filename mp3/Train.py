from Digits import * 
from Test import *

class Train:
	def __init__(self, fname):
		self.num_array = None #holds 0s or 1s as in input file
		self.num_digits = None 
		self.curDigit = None
		self.priors = None #array of priors
		self.Digits = None #digits object that hold information for class for each digit (0-9)
		self.classAccuracy = None #classification accuracy probabilities

		self.fname = fname

		self.readFile()
		self.calcPriors()

	def readFile(self):
		self.num_array = []
		self.num_digits = []
		self.Digits = []
		self.classAccuracy = []

		a = 0 #initializes digits objects
		while (a < 10):
			digit = Digits()
			self.num_digits.append(0)
			self.Digits.append(digit)
			a += 1

		with open(self.fname) as f: #read in train file
		    	content = f.readlines()
		content = [x.strip() for x in content]
		counter = 0

		for line in content: #initializes num array
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
		cc = 0 #calculates zero probabilities
		while cc < 10:
			#print ("--------------------------------------------------------------------------------------------")
			self.Digits[cc].division()
			self.Digits[cc].convertToOne()
			cc += 1

	def calcPriors(self): #calculates priors
		self.priors = []

		total = 0
		for val in self.num_digits:
			total = total + val

		for val in self.num_digits:
			prob = val/total
			self.priors.append(prob)

		print('Below are the priors.')
		print(self.priors)

if __name__ == "__main__":
	train = Train('digitdata/digitdata/optdigits-orig_train.txt')
	test = Test('digitdata/digitdata/optdigits-orig_test.txt', train)
	print (train.num_digits)
