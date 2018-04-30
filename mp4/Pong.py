import sys, pygame
import random
import decimal
from Space import *

pygame.init()

Gsize = Gwidth, Gheight = 620, 600
white = 250, 250, 250
black = 0, 0, 0
red = 255, 0, 0

paddle_y = 240
pos = [300, 300]
rect = pygame.Rect(600, paddle_y, 20, 120)
velocity = [6, 0]
screen = pygame.display.set_mode(Gsize)

contGame = True

while (contGame == True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pos[0] = pos[0] + velocity[0]
    pos[1] = pos[1] + velocity[1]

    if pos[1] < 0:
    	pos[1] = (-1 * pos[1])
    	velocity[1] = -1 * velocity[1]
    elif pos[1] > 600:
    	pos[1] = (1200 - pos[1])
    	velocity[1] = -1 * velocity[1]

    if pos[0] < 0:
    	pos[0] = (-1 * pos[0])
    	velocity[0] = -1 * velocity[0]

    if (pos[0] > 600) and (pos[1] > paddle_y) and (pos[1] < (paddle_y+120)):
    	pos[0] = 1200 - pos[0]
    	u = (decimal.Decimal(random.randrange(-9, 9)))
    	v = (decimal.Decimal(random.randrange(-18, 18)))
    	velocity[0] = (-1*velocity[0]) + u
    	velocity[1] = velocity[1] + v
    elif (pos[0] > 600):
    	contGame = False


    screen.fill(black)
    pygame.draw.circle(screen, red, pos, 25, 0)
    pygame.draw.rect(screen, white, rect, 0)
    pygame.display.flip()
