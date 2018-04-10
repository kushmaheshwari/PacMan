from Digits import *
from Train import *
#from matplotlib import colors, pyplot

class Perceptron:
	def __init__(self, fname, train):
		self.num_array = None #holds 0s or 1s as in input file
		self.curDigit = None
		self.classAccuracy = None #classification accuracy probabilities
		self.idx = None
		self.train = train
		self.matrix = None #holds counts of guessed vs actual class
		self.percentageMatrix = None #holds percentages of probabilities of matrix
		self.oddsMatrix = None #holds odd ratio matrix

		self.sumError = 0
		self.lRate = 0.5

		self.fname = fname

		self.initializeMatrix()
		self.readTrainFile()


	def readTrainFile(self):
		self.num_array = []
		self.classAccuracy = []
		totalError = []

		a = 0 #initializes digits objects

		with open(self.fname) as f: #read in train file
		    	content = f.readlines()
		content = [x.strip() for x in content]
		counter = 0
		epoch = 0


		while epoch < 15:
			epoch += 1

			cc = 0 
			while cc < 10:#Resets the correct guesses and total guesses at every epoch because we only want the final class accuracy
				digital = self.train.Digits[cc]
				digital.correctGuesses = 0
				digital.totalGuesses = 0
				self.initializeMatrix()
				cc += 1

			self.sumError = 0 #The total error for the current epoch
			for line in content: #initializes num array
				row = []

				counter += 1
				for character in line:
					if (counter == 33): #looks at what class the image belongs (looks at digit)
						counter = 0
						self.idx = self.predict(self.num_array) #Guesses the number based on the predict function
						digit = self.train.Digits[int(character)]
						digit.totalGuesses += 1
						self.updateConfusion(character)

						if (self.idx == int(character)): #If correct do not update weights
							digit.correctGuesses += 1
						else:#However if incorrect...
							self.sumError += 1
							digit.updateWeights(self.lRate, 1, self.num_array) #Update the digit it was supposed to be and make its weights stronger
							self.train.Digits[self.idx].updateWeights(self.lRate, -1, self.num_array) #update the incorrect digit and make its weights weaker
						
						self.num_array = [] #reset the array


					else:
						row.append(int(character))

				if (counter != 0):
					self.num_array.append(row)

			totalError.append((1 - (self.sumError/2432))*100) #append the epoch accuracy
			print(self.lRate)
			self.lRate = self.lRate / 2 #have the learning rate every time
			

		#cmap2 = colors.LinearSegmentedColormap.from_list('my_colormap', #The color map for our weight visualization
                                          # ['white','black','red'],
                                          # 256)

		cc = 0 
		while cc < 10:
			digital = self.train.Digits[cc]
			self.train.classAccuracy.append(digital.correctGuesses/digital.totalGuesses)


			#img2 = pyplot.imshow(digital.weights, interpolation='nearest', #create the plot
             #       cmap = cmap2,
              #      origin='lower')

			#pyplot.colorbar(img2,cmap=cmap2)

			#pyplot.show()
			#print(digital.weights)
			cc += 1

		#print('Below is the class accuracy.')
		#print(self.train.classAccuracy)

		#print('Below is the accuracy for each epoch')
		#print(totalError)

		self.calcPercentages(self.matrix)

	def predict(self, num_array): #This predicts the image number based on the weights of all the digit classes
		guesses = []

		cc = 0
		while cc < 10:

			total = self.train.Digits[cc].bias

			a = 0
			while a < 32:
				b = 0
				row = num_array[a]
				digitRow = self.train.Digits[cc].weights[a]
				while b < 32:
					total += row[b]*digitRow[b] #The total will equal the bias + the weight of a pixel times the pixel (0 or 1)
					b += 1
				a += 1
			guesses.append(total)
			cc += 1
		#print(guesses)
		return guesses.index(max(guesses)) #Returns the max guess which correlates to most likely number

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

	def updateConfusion(self, character): #counts guessed digits given what digits it should actually be
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
				value = item/self.train.Digits[index].totalGuesses
				line.append('%.3f' % value)
			self.percentageMatrix.append(line)

		print('Below is the confusion matrix.')
		print(self.percentageMatrix)