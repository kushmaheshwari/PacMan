import sys, pygame, time
import random
import decimal
from QL import *
import numpy as np


Gsize = Gwidth, Gheight = 620, 600
white = 250, 250, 250
black = 0, 0, 0
red = 255, 0, 0

QL = QL()
gamma = 0.8

paddle_y = 240
pos = [300, 300]
rect = pygame.Rect(600, paddle_y, 20, 120)
velocity = [18, 0]

pygame.init()
screen = pygame.display.set_mode(Gsize)

contGame = 100000
bounces = 0
reward = 0

while (contGame > 0):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	#time.sleep(.02)

	#print("yo")
	#print (QL.QMatrix[11, 6, 1, 1, 1])
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

	dPaddle = (paddle_y + 60)//50
	possibleAction = QL.bestAction(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle)
	possibleAction -= 1
	
	#possibleAction = random.randrange(-1,2)
	#print('Best Action')
	#print(possibleAction)
	if (possibleAction == -1 and paddle_y > 1):
		paddle_y = paddle_y - 24
	if (possibleAction == 1 and paddle_y < 479):
		paddle_y = paddle_y + 24

	pos[0] = pos[0] + velocity[0]
	pos[1] = pos[1] + velocity[1]

	if pos[1] < 0:
		pos[1] = (-1 * pos[1])
		velocity[1] = -1 * velocity[1]
	elif pos[1] >= 600:
		pos[1] = (1199 - pos[1])
		velocity[1] = -1 * velocity[1]
	if pos[0] < 0:
		pos[0] = (-1 * pos[0])
		velocity[0] = -1 * velocity[0]

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
		QL.updateQMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward)
	elif (pos[0] >= 600):
		reward = -1
		print('Bounces' + str(bounces))
		print(contGame)
		bounces = 0
		contGame -= 1
		#print('Failed')
		pos[0] = 599
		QL.updateQMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward)
		paddle_y = 240
		pos = [300, 300]
		velocity = [18, 0]
	else:
		reward = 0
		QL.updateQMatrix(pos[0]//50, pos[1]//50, dVel[0], dVel[1], dPaddle, possibleAction, reward)

	screen.fill(black)
	pygame.draw.circle(screen, red, pos, 25, 0)
	rect = pygame.Rect(600, paddle_y, 20, 120)	
	pygame.draw.rect(screen, white, rect, 0)
	pygame.display.flip()
	#print (contGame)

