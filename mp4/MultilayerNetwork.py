class MultilayerNetwork:
	def __init__(self, fname):
		self.num_array = None #holds 0s or 1s as in input file
		self.curDigit = None
		self.classAccuracy = None #classification accuracy probabilities
		self.idx = None
		self.matrix = None #holds counts of guessed vs actual class
		self.percentageMatrix = None #holds percentages of probabilities of matrix
		self.oddsMatrix = None #holds odd ratio matrix

		self.sumError = 0
		self.lRate = 0.5

		self.fname = fname

		self.initializeMatrix()
		self.readTrainFile()


	def readTrainFile(self):
		with open(self.fname) as f: #read in train file
		    	content = f.readlines()
		content = [x.strip() for x in content]
		counter = 0
		epoch = 0

		while epoch < 15:
			epoch += 1

			self.sumError = 0 #The total error for the current epoch
			for line in content: #initializes num array
				row = []

				line.split()
				print(line)

if __name__ == "__main__":
	MultilayerNetwork = MultilayerNetwork('ExpertPolicy.txt')
