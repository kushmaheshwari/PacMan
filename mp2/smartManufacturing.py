from queue import *

class smartManufacturing:
	def __init__(self):
		self.widgets = None

		self.initialize()

	def initialize(self):
		widget1 = ["A","E","D","C","A"]
		widget2 = ["B","E","A","C","D"]
		widget3 = ["B","A","B","C","E"]
		widget4 = ["D","A","D","B","D"]
		widget5 = ["B","E","C","B","D"]

		queue1 = Queue(maxsize=0)
		for item in widget1:
			queue1.put(item)

		queue2 = Queue(maxsize=0)
		for item in widget2:
			queue2.put(item)

		queue3 = Queue(maxsize=0)
		for item in widget3:
			queue3.put(item)

		queue4 = Queue(maxsize=0)
		for item in widget4:
			queue4.put(item)

		queue5 = Queue(maxsize=0)
		for item in widget5:
			queue5.put(item)	

		self.widgets = []
		self.widgets.append(queue1)
		self.widgets.append(queue2)
		self.widgets.append(queue3)
		self.widgets.append(queue4)
		self.widgets.append(queue5)









