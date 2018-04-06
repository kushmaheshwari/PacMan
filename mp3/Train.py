

class Train:
	def __init__(self, fname):
		self.num_array = None
		self.num_digits = None
		self.curDigit = None
		self.priors = None

		self.fname = fname

		self.readFile()
		self.calcPriors()

	def readFile(self):
		self.num_array = []
		self.num_digits = []

		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)
		self.num_digits.append(0)

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
				else:
					row.append(int(character))
			self.num_array.append(row)

	def calcPriors():
		self.priors = []

		total = 0
		for val in self.num_digits:
			total = total + val

		for val in self.num_digits:
			

if __name__ == "__main__":
	train = Train('digitdata/digitdata/optdigits-orig_train.txt')
	print (train.num_digits)
