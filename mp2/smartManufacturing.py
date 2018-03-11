class smartManufacturing:

	def __init__(self):
		self.widgets = None
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
		widget1 = ["A","E","D","C","A"]
		widget2 = ["B","E","A","C","D"]
		widget3 = ["B","A","B","C","E"]
		widget4 = ["D","A","D","B","D"]
		widget5 = ["B","E","C","B","D"]

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

