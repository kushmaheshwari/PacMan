class smartManufacturing:

	def __init__(self):
		self.widgets = None

		self.letters = []
		self.totalLetters = 0
		
		self.initialize()

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
