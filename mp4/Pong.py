import sys, pygame

pygame.init()

Gsize = Gwidth, Gheight = 600, 600
Bsize = Bwidth, Bheight = 50, 50
white = 250, 250, 250
black = 0, 0, 0
red = 255, 0, 0
pos = [300, 300]
velocity = [3, 1]
screen = pygame.display.set_mode(Gsize)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pos[0] = pos[0] + velocity[0]
    pos[1] = pos[1] + velocity[1]

    screen.fill(black)
    pygame.draw.circle(screen, red, pos, 25, 0)
    pygame.display.flip()