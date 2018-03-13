import random

def generate(n):
	widget1 = []
	widget2 = []
	widget3 = []
	widget4 = []
	widget5 = []
	let = ["A", "B", "C", "D", "E"]

	i = n
	while i > 0:
		widget1.append(random.choice(let))
		i = i - 1

	i = n
	while i > 0:
		widget2.append(random.choice(let))
		i = i - 1

	i = n
	while i > 0:
		widget3.append(random.choice(let))
		i = i - 1

	i = n
	while i > 0:
		widget4.append(random.choice(let))
		i = i - 1

	i = n
	while i > 0:
		widget5.append(random.choice(let))
		i = i - 1

	widgets = []
	widgets.append(widget1)	
	widgets.append(widget2)
	widgets.append(widget3)
	widgets.append(widget4)
	widgets.append(widget5)

	return widgets


class smartManufacturing:

	def __init__(self, widgets):
		self.widgets = widgets
		self.widgetsNum = None
		self.distances = None
		self.heuristics = None

		self.letters = []
		self.maxHeuristic = []
		self.totalLetters = 0
		self.totalDistance = 0

		self.initialize()
		self.letToNum()
		self.calcHeuristic()

	def initialize(self):
		

		#print(widget1, widget2, widget3, widget4, widget5)

		widget1 = ["A","D","C","B","A","D","B","B"]
		widget2 = ["D","A","D","C","D","E","A","B"]
		widget3 = ["C","C","A","E","B","D","C","E"]
		widget4 = ["D","C","A","C","D","A","B","D"]
		widget5 = ["A","C","E","D","C","D","B","A"]

		self.widgets = []
		self.widgets.append(widget1)	
		self.widgets.append(widget2)
		self.widgets.append(widget3)
		self.widgets.append(widget4)
		self.widgets.append(widget5)

		
		self.letters.append(0)
		self.letters.append(0)
		self.letters.append(0)
		self.letters.append(0)
		self.letters.append(0)

		self.maxHeuristic.append(0)
		self.maxHeuristic.append(0)
		self.maxHeuristic.append(0)
		self.maxHeuristic.append(0)
		self.maxHeuristic.append(0)

		fromA = [0, 1064, 673, 1401, 277]
		fromB = [1064, 0, 958, 1934, 337]
		fromC = [673, 958, 0, 1001, 399]
		fromD = [1401, 1934, 1001, 0, 387]
		fromE = [277, 337, 399, 387, 0]

		self.distances = []
		self.distances.append(fromA)
		self.distances.append(fromB)
		self.distances.append(fromC)
		self.distances.append(fromD)
		self.distances.append(fromE)

	def letToNum(self):
		self.widgetsNum = []

		for index, item in enumerate(self.widgets):
			emptyarray = []
			for idx in item:
				if (idx == 'A'):
					emptyarray.append(0)
				if (idx == 'B'):
					emptyarray.append(1)
				if (idx == 'C'):
					emptyarray.append(2)
				if (idx == 'D'):
					emptyarray.append(3)
				if (idx == 'E'):
					emptyarray.append(4)
			self.widgetsNum.append(emptyarray)

	def calcHeuristic(self):
		self.heuristics = []
		for item in self.widgetsNum:
			emptyarray = []
			j = 5
			prev = 0
			for index in reversed(item):
				if j == 5:
					emptyarray.append(0)
				else:
					intermed = self.distances[index]
					prev = intermed[j] + prev
					emptyarray.append(prev)
				j = index
			emptyarray.reverse()
			self.heuristics.append(emptyarray)

