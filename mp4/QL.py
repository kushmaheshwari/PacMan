import numpy as np
import random

class QL:
	def __init__(self):
		self.gamma = 0.8
		self.alpha = 0.2
		self.QMatrix = np.zeros((12, 12, 2, 3, 12, 3))
		self.NMatrix = np.zeros((12, 12, 2, 3, 12, 3))
		self.GameOver = 0

	def updateQMatrix(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y, possibleAction, reward):
		ball_x = int(ball_x)
		ball_y = int(ball_y)
		pos = [ball_x, ball_y]
		velocity = [velocity_x, velocity_y]
		pos[0] = pos[0] + velocity[0]
		pos[1] = pos[1] + velocity[1]

		if pos[1] < 0:
			pos[1] = (-1 * pos[1])
			velocity[1] = -1 * velocity[1]
		elif pos[1] > 11:
			pos[1] = (23 - pos[1])
			velocity[1] = -1 * velocity[1]

		if pos[0] < 0:
			pos[0] = (-1 * pos[0])
			velocity[0] = -1 * velocity[0]

		if (pos[0] > 11) and (pos[1] == paddle_y):
			pos[0] = 23 - pos[0]
			velocity[0] = -1 * velocity[0]

		if velocity_x < 0:
			velocity_x = 0
		if velocity[0] < 0:
			velocity[0] = 0
	
		possibleAction += 1
		#print('Print Values of Actions at current State')
		#print(ball_x, ball_y, pos[0], pos[1], velocity_x, velocity_y, velocity[0], velocity[1], paddle_y, possibleAction)
		#print(self.QMatrix[ball_x, ball_y, velocity_x, velocity_y, paddle_y])
		#print(ball_x, ball_y, velocity_x, velocity_y, paddle_y)
		if (pos[0] > 11) and (pos[1] != paddle_y):
			#print('SuperFailed')
			#self.GameOver -= 1
			#print (reward)
			self.QMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] += reward
			self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] += 1

			#print (self.QMatrix[ball_x, ball_y, velocity_x, velocity_y+1, paddle_y, possibleAction])
			#print (self.QMatrix[ball_x, ball_y, velocity_x, velocity_y+1, paddle_y])
		
		elif(pos[0] < 12):# ball_x < 12):
			#print(reward + max(self.QMatrix[pos[0], pos[1], velocity[0], velocity[1]+1, paddle_y]))
			self.alpha = 50/(50 + self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction])

			change = self.QMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] 
			self.QMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] = change + self.alpha*(reward + self.gamma*max(self.QMatrix[pos[0], pos[1], velocity[0], velocity[1]+1, paddle_y]) - change)
			self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] += 1
			print(self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])

	def bestAction(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y):
		ball_x = int(ball_x)
		ball_y = int(ball_y)
		if velocity_x < 0:
			velocity_x = 0
		#print('Best')
		#print(ball_x, ball_y, velocity_x, velocity_y, paddle_y)
		#print (self.QMatrix[ball_x, ball_y, velocity_x, velocity_y+1, paddle_y]) 
		randomInt = random.randrange(0, 10)
		print('Threshold :' + str(20//(np.max(self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])+1)))
		if randomInt < 20//(np.max(self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])+1):
			return random.randrange(0, 3)
		else:
			print('Argmax')
			print(self.QMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])
			return np.argmax(self.QMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y]) 

