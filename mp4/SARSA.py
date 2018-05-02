import numpy as np
import random

class SARSA:
	def __init__(self):
		self.gamma = 0.77
		self.alpha = 0
		self.SARSAMatrix = np.zeros((12, 12, 2, 3, 12, 3))
		self.NMatrix = np.zeros((12, 12, 2, 3, 12, 3))
		self.epsilon = 0
		self.GameOver = 0

	def updateSARSAMatrix(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y, possibleAction, reward, count):
		#discretize ball position
		ball_x = int(ball_x)
		ball_y = int(ball_y)
		pos = [ball_x, ball_y]
		velocity = [velocity_x, velocity_y]
		#move ball based on velocity
		pos[0] = pos[0] + velocity[0]
		pos[1] = pos[1] + velocity[1]
		#keep paddle from moving off of screen
		newPaddle_y = paddle_y + possibleAction
		if (newPaddle_y == 12):
			newPaddle_y = 11
		if (newPaddle_y == -1):
			newPaddle_y = 0

		#change ball velocity when ball hits the wall
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

		nextAction = self.bestAction(pos[0], pos[1], velocity[0], velocity[1], newPaddle_y, count)
		#print('Print Values of Actions at current State')
		#print(ball_x, ball_y, pos[0], pos[1], velocity_x, velocity_y, velocity[0], velocity[1], paddle_y, possibleAction)
		#print(self.QMatrix[ball_x, ball_y, velocity_x, velocity_y, paddle_y])
		#print(ball_x, ball_y, velocity_x, velocity_y, paddle_y)

		#calculate alpha value
		self.alpha = 1/(1 + self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction])

		#check if ball is by paddle
		if (pos[0] > 11) and (pos[1] != paddle_y):
			#print (reward)
			#calculate Q(s, a)
			change = self.SARSAMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] 
			new = change + self.alpha*(reward - self.gamma - change)
			self.SARSAMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] = new
			if new != 0:
				self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] += 1
		
		elif(pos[0] < 12):

			change = self.SARSAMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] 
			#Q(s, a) <-- Q(s, a) + alpha(r(s) + gamma*(Q(s2,a2)) - Q(s,a)) 
			new = change + self.alpha*(reward + self.gamma*self.SARSAMatrix[pos[0]][pos[1]][velocity[0]][velocity[1]+1][newPaddle_y][nextAction] - change)
			self.SARSAMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] = new
			if new != 0:
				self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y][possibleAction] += 1
			#print(self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])

	#selects action to take
	def bestAction(self, ball_x, ball_y, velocity_x, velocity_y, paddle_y, count):
		ball_x = int(ball_x)
		ball_y = int(ball_y)
		if velocity_x < 0:
			velocity_x = 0
		#print('Best')
		#print(ball_x, ball_y, velocity_x, velocity_y, paddle_y)
		#print (self.QMatrix[ball_x, ball_y, velocity_x, velocity_y+1, paddle_y]) 
		#randomInt = random.randrange(0, 10)
		#print('Threshold :' + str(10000//(np.min(self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])+1)))
		
		#decides random value to determine exploration vs exploitation
		#if (np.max(self.NMatrix[ball_x-1][ball_y][velocity_x][velocity_y+1][paddle_y]) - np.min(self.NMatrix[ball_x-1][ball_y][velocity_x][velocity_y+1][paddle_y])) < .1:
		if count < 20000: #1000 > (np.min(self.NMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])):
			rint = random.randrange(0, 3)
			#print ('Random')
			return rint

		#exploitation
		else:
			#print('Argmax')
			#print(self.QMatrix[ball_x][ball_y][velocity_x][velocity_y+1][paddle_y])
			return np.argmax(self.SARSAMatrix[ball_x-1][ball_y][velocity_x][velocity_y+1][paddle_y]) 

