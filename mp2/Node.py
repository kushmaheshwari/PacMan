class Node:
	def __init__(self, letter, value, h, phrase):
		self.letter = letter
		self.phrase = phrase
		self.h = h
		self.value = value

	def __lt__(self, other):
		if (self.value < other.value):
			return self
		return other