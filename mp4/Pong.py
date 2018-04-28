import sys, pygame
import time

pygame.init()

Gsize = Gwidth, Gheight = 600, 600

white = 250, 250, 250
black = 0, 0, 0
red = 255, 0, 0

paddle_y = 240
pos = [300, 300]
rect = pygame.Rect(580, paddle_y, 20, 120)
velocity = [18, 6]
screen = pygame.display.set_mode(Gsize)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pos[0] = pos[0] + velocity[0]
    pos[1] = pos[1] + velocity[1]

    time.sleep(.100)

    screen.fill(black)
    pygame.draw.circle(screen, red, pos, 10, 0)
    pygame.draw.rect(screen, white, rect, 0)
    pygame.display.flip()