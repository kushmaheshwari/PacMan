import numpy as np
import math

class MultilayerNetwork:
	def __init__(self, fname):
		self.scalar = .25
		self.weightOne = np.random.randn(5, 256) * self.scalar
		self.weightTwo = np.random.randn(256, 256) * self.scalar
		self.weightThree = np.random.randn(256, 256) * self.scalar
		self.weightFour = np.random.randn(256, 3) * self.scalar
		self.biasOne = np.zeros((256))
		self.biasTwo = np.zeros((256))
		self.biasThree = np.zeros((256))
		self.biasFour = np.zeros((3))

		self.mean = 0

		self.batchSize = 100

		self.lRate = 0.1

		self.fname = fname

		self.readFile()

	def readFile(self):
		with open(self.fname) as f: #read in train file
		    	content = f.readlines()
		content = [x.strip() for x in content]
		
		epoch = 0

		while epoch < 15:
			epoch += 1
			rowInput = np.zeros((100, 5))
			rowOutput = np.zeros((100, 1))
			counter = 0
	
			for line in content: #initializes num array
				data = line.split()
				dataInput = data[:-1]
				dataOutput = data[5:]
				rowInput[counter]= dataInput
				rowOutput[counter] = dataOutput
				
				if counter == self.batchSize - 1:
					n = 0
					while n < 5:
						self.mean = np.mean(rowInput[:,n])
						rowInput[:, n] -= self.mean
						rowInput[:, n] = rowInput[:, n]/np.std(rowInput[:, n])
						n += 1

					row1 = rowInput
					intOne = self.affineForward(row1, self.weightOne, self.biasOne)
					row2 = self.reluForward(intOne)
					intTwo = self.affineForward(row2, self.weightTwo, self.biasTwo)
					row3 = self.reluForward(intTwo)
					intThree = self.affineForward(row3, self.weightThree, self.biasThree)
					row4 = self.reluForward(intThree)
					intFour = self.affineForward(row4, self.weightFour, self.biasFour)

					Loss, dintFour = self.crossEntropy(intFour, rowOutput)

					drow4, dweightFour, dbiasFour = self.affineBackward(dintFour, 100, 256)



					rowInput = np.zeros((100, 5))
					rowOutput = np.zeros((100, 1))
					counter = 0
				counter += 1

	def affineForward(self, row, weight, bias):
		inter = np.dot(row, weight)
		return (inter + bias)

	def reluForward(self, inter):
		return inter.clip(0, 100)

	def crossEntropy(self, intFour, rowOutput):
		n = 0
		totalLoss = 0
		totalGrad = np.zeros((100, 3))
		while n < self.batchSize:
			idx = int(rowOutput[n])
			x = 0
			sumF = 0
			while x < 3:
				#print(math.exp(intFour[n][x]))
				sumF += math.exp(intFour[n][x])
				x += 1
			totalLoss += intFour[n][idx] - math.log(sumF)


			x = 0
			while x < 3:
				if x == idx:
					totalGrad[n][x] = -(1 - math.exp(intFour[n][x])/sumF)/self.batchSize
				else:
					totalGrad[n][x] = -(0 - math.exp(intFour[n][x])/sumF)/self.batchSize
				x += 1
			
			n += 1
		totalLoss = totalLoss/self.batchSize

		return totalLoss, totalGrad

	def affineBackward(self, F, i, j):
		n = 0
		sum = 0
		drow4 = np.zeros((i, j))
		while n < 3:
			print(F.shape)
			print(self.weightFour.shape)
			drow4 += np.dot(F[n], self.weightFour[n])
			n += 1

		print(drow4)
		dweightFour = np.zeros
		n = 0
		while n < self.batchSize:



if __name__ == "__main__":
	MultilayerNetwork = MultilayerNetwork('ExpertPolicy.txt')
