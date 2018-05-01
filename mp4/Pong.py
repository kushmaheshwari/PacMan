import sys, pygame, time
import math
import random
import decimal
from QL import *
import numpy as np
from SARSA import *

#initalize game space
Gsize = Gwidth, Gheight = 620, 600
white = 250, 250, 250
black = 0, 0, 0
red = 255, 0, 0

graph = np.zeros((500))
idx = 0

#QL = QL()
SARSA = SARSA()

paddle_y = 240
#inititalize ball_x and ball_y
pos = [300, 300]
#initialize paddle
rect = pygame.Rect(600, paddle_y, 20, 120)
#initialize velocity_x and velocity_y
velocity = [18, 6]

#pygame.init()
#screen = pygame.display.set_mode(Gsize)

#iteration count
contGame = 0
totalBounces = 0
bounces = 0
#total reward
reward = 0

while (contGame < 40000):
	#for event in pygame.event.get():
	#	if event.type == pygame.QUIT: sys.exit()

	#time.sleep(.02)

	#print("yo")
	#print (QL.QMatrix[11, 6, 1, 1, 1])

	#discretize velocity
	dVel = [velocity[0], velocity[1]]
	if velocity[0] > 0:
		dVel[0] = 1
	else:
		dVel[0] = -1
	if velocity[1] > 9:
		dVel[1] = 1
	elif velocity[1] < -9:
		dVel[1] = -1
	else:
		dVel[1] = 0

	#discretize paddle
	dPaddle = math.floor(12*paddle_y/(600-120))
	if dPaddle == 12:
		dPaddle = 11

	#select action to take
	possibleAction = SARSA.bestAction(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, contGame)
	possibleAction -= 1
	
	#possibleAction = random.randrange(-1,2)
	#print('Best Action')
	#print(possibleAction)

	#move paddle based on selected action
	if (possibleAction == -1 and paddle_y > 1):
		paddle_y = paddle_y - 24
	if (possibleAction == 1 and paddle_y < 479):
		paddle_y = paddle_y + 24

	#change position of ball based on its velocity
	pos[0] = pos[0] + velocity[0]
	pos[1] = pos[1] + velocity[1]

	#change velocity if ball hits a wall
	if pos[1] < 0:
		pos[1] = (-1 * pos[1])
		velocity[1] = -1 * velocity[1]
	elif pos[1] >= 600:
		pos[1] = (1199 - pos[1])
		velocity[1] = -1 * velocity[1]
	if pos[0] < 0:
		pos[0] = (-1 * pos[0])
		velocity[0] = -1 * velocity[0]

	#when ball hits the paddle
	if (pos[0] >= 600) and (pos[1] > paddle_y) and (pos[1] < (paddle_y+120)):
		reward = 1
		bounces += 1
		totalBounces += 1
		pos[0] = 1199 - pos[0]
		#randomize velocity when the ball hits the paddle
		u = (decimal.Decimal(random.randrange(-9, 9)))
		v = (decimal.Decimal(random.randrange(-18, 18)))
		velocity[0] = (-1*velocity[0]) + u
		velocity[1] = velocity[1] + v
		if (velocity[0] > -18):
			velocity[0] = -18
		#q-learning/sarsa - update rewards
		SARSA.updateSARSAMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward, contGame)
	#whn ball passes the paddle
	elif (pos[0] >= 600):
		reward = -1
		print('Bounces' + str(bounces))
		print(contGame)
		bounces = 0
		contGame += 1
		if contGame % 200 == 0:
			graph[idx] = totalBounces
			idx += 1
			totalBounces = 0
		#print('Failed')
		pos[0] = 599
		#q-learning/sarsa - update rewards
		SARSA.updateSARSAMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward, contGame)
		#re-initalize game
		paddle_y = 240
		pos = [300, 300]
		velocity = [18, 6]
	else:
		reward = 0
		#q-learning/sarsa - update rewards
		SARSA.updateSARSAMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward, contGame)

	#screen.fill(black)
	#pygame.draw.circle(screen, red, pos, 25, 0)
	#rect = pygame.Rect(600, paddle_y, 20, 120)	
	#pygame.draw.rect(screen, white, rect, 0)
	#pygame.display.flip()
	#print (contGame)

#np.savetxt("foo2.csv", graph, delimiter=", ")

#run after 100,000 training trials
print(totalBounces/10000)
pygame.init()
screen = pygame.display.set_mode(Gsize)

while (True):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	time.sleep(.02)

	#print("yo")
	#print (QL.QMatrix[11, 6, 1, 1, 1])

	#discretize velocity
	dVel = [velocity[0], velocity[1]]
	if velocity[0] > 0:
		dVel[0] = 1
	else:
		dVel[0] = -1
	if velocity[1] > 9:
		dVel[1] = 1
	elif velocity[1] < -9:
		dVel[1] = -1
	else:
		dVel[1] = 0

	#discretize paddle position
	dPaddle = math.floor(12*paddle_y/(600-120))
	if dPaddle == 12:
		dPaddle = 11

	#select action
	possibleAction = SARSA.bestAction(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, contGame)
	possibleAction -= 1
	
	#possibleAction = random.randrange(-1,2)
	#print('Best Action')
	#print(possibleAction)

	#move paddle based on action picked
	if (possibleAction == -1 and paddle_y > 1):
		paddle_y = paddle_y - 24
	if (possibleAction == 1 and paddle_y < 479):
		paddle_y = paddle_y + 24

	#move ball based on velocity
	pos[0] = pos[0] + velocity[0]
	pos[1] = pos[1] + velocity[1]

	#change velocity if ball hit the wall
	if pos[1] < 0:
		pos[1] = (-1 * pos[1])
		velocity[1] = -1 * velocity[1]
	elif pos[1] >= 600:
		pos[1] = (1199 - pos[1])
		velocity[1] = -1 * velocity[1]
	if pos[0] < 0:
		pos[0] = (-1 * pos[0])
		velocity[0] = -1 * velocity[0]

	#when ball hits the paddle
	if (pos[0] >= 600) and (pos[1] > paddle_y) and (pos[1] < (paddle_y+120)):
		reward = 1
		bounces += 1
		pos[0] = 1199 - pos[0]
		u = (decimal.Decimal(random.randrange(-9, 9)))
		v = (decimal.Decimal(random.randrange(-18, 18)))
		velocity[0] = (-1*velocity[0]) + u
		velocity[1] = velocity[1] + v
		if (velocity[0] > -18):
			velocity[0] = -18
		#update rewards
		SARSA.updateSARSAMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward, contGame)
	
	#when ball goes past the paddle
	elif (pos[0] >= 600):
		reward = -1
		print('Bounces' + str(bounces))
		print(contGame)
		bounces = 0
		contGame -= 1
		#print('Failed')
		pos[0] = 599
		#update rewards
		SARSA.updateSARSAMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward, contGame)
		paddle_y = 240
		pos = [300, 300]
		velocity = [18, 6]
	else:
		reward = 0
		#update rewards
		SARSA.updateSARSAMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward, contGame)

	#specs for game 
	screen.fill(black)
	pygame.draw.circle(screen, red, pos, 25, 0)
	rect = pygame.Rect(600, paddle_y, 20, 120)	
	pygame.draw.rect(screen, white, rect, 0)
	pygame.display.flip()
	#print (contGame)


