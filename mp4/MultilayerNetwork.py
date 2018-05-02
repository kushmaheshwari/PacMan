import numpy as np
import math

class MultilayerNetwork:
	def __init__(self, fname, testfile):
		self.scalar = .00001
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

		self.testfile = testfile

		self.losses = np.zeros((10))
		self.accuracy = np.zeros((250, 2))
		self.realAccuracy = np.zeros((10))

		#self.testFile()

		self.readFile()

	def testFile(self):
		with open(self.testfile) as f: #read in train file
		    	content = f.readlines()
		content = [x.strip() for x in content]
		row = np.zeros((10, 8))
		weight = np.zeros((8, 4))
		bias = np.zeros((1, 4))
		dZ = np.zeros((10, 4))
		counter = 0
		x = 0
		for line in content: #initializes num array	
			data = line.split()
			#print(counter)
			#print(data)
			if (x > 0) and (x < 11):
				row[counter] = data
				counter += 1
			if x == 13 or x == 23 or x == 36:
				counter = 0
			if x > 12 and x < 21:
				weight[counter] = data
				counter += 1
			if x == 23:
				bias[0] = data
			if x == 25:
				intOne = self.affineForward(row, weight, bias)
				print('intOne')
				print(intOne)
			if x > 37 and x < 48:
				dZ[counter] = data
				counter += 1
			if x == 50:
				dA, dW, db = self.affineBackward(dZ, weight, row)
				print('dA')
				print(dA)
				print('dW')
				print(dW)
				print('dB')
				print(db)
			x += 1

			




	def readFile(self):
		with open(self.fname) as f: #read in train file
		    	content = f.readlines()
		content = [x.strip() for x in content]
		
		epoch = 0

		while epoch < 10:

			print(epoch)
			epoch += 1
			rowInput = np.zeros((100, 5))
			rowOutput = np.zeros((100, 1))
			counter = 0
	
			i = 0
			for line in content: #initializes num array
				data = line.split()
				dataInput = data[:-1]
				dataOutput = data[5:]
				rowInput[counter]= dataInput
				rowOutput[counter] = dataOutput

				acc = 0
				
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

					x = 0
					
					while x < self.batchSize:
						if np.argmax(intFour[x]) == rowOutput[x]:
							acc += 1
						x += 1

					#print(acc/100)
					Loss, dintFour = self.crossEntropy(intFour, rowOutput)

					drow4, dweightFour, dbiasFour = self.affineBackward(dintFour, self.weightFour, row4)
					dintThree = self.reluBackward(drow4, row4)
					drow3, dweightThree, dbiasThree = self.affineBackward(dintThree, self.weightThree, row3)
					dintTwo = self.reluBackward(drow3, row3)
					drow2, dweightTwo, dbiasTwo = self.affineBackward(dintTwo, self.weightTwo, row2)
					dintOne = self.reluBackward(drow2, row2)
					drow1, dweightOne, dbiasOne = self.affineBackward(dintOne, self.weightOne, row1)

					self.weightOne -= self.lRate*dweightOne
					self.weightTwo -= self.lRate*dweightTwo
					self.weightThree -= self.lRate*dweightThree
					self.weightFour -= self.lRate*dweightFour

					self.biasOne -= self.lRate*dbiasOne
					self.biasTwo -= self.lRate*dbiasTwo
					self.biasThree -= self.lRate*dbiasThree
					self.biasFour -= self.lRate*dbiasFour

					rowInput = np.zeros((100, 5))
					rowOutput = np.zeros((100, 1))
					counter = 0

					self.realAccuracy[i] = acc/100
					self.losses[i] = Loss
				counter += 1
				
			self.accuracy[epoch][0] = np.mean(self.losses)
			self.accuracy[epoch][1] = np.mean(self.realAccuracy)

		np.savetxt("foo5.csv", self.accuracy, delimiter=", ")

	def affineForward(self, row, weight, bias):
		print (row)
		print (weight)
		print (bias)
		inter = np.dot(row, weight)
		return (inter + bias)

	def reluForward(self, inter):
		return inter.clip(0, 100000000)

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
		totalLoss = -totalLoss/self.batchSize

		return totalLoss, totalGrad

	def affineBackward(self, F, weight, row): #100, 256, 3
		drow = np.dot(F, weight.transpose())
		dweight = np.dot(row.transpose(), F)
		dbias = F.sum(axis = 0)

		return drow, dweight, dbias

	def reluBackward(self, inter, row):
		n = 0
		while n < len(row):
			x = 0
			while x < len(row[n]):
				if row[n][x] == 0:
					inter[n][x] = 0
				x += 1
			n += 1
		return inter

if __name__ == "__main__":
	MultilayerNetwork = MultilayerNetwork('ExpertPolicy.txt', 'affine.txt')
