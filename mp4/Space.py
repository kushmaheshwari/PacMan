import pygame

def defineState(ball_x, ball_y, velocity_x, velocity_y, paddle_y):
	posx = int(ball_x/50)
	posy = int(ball_y/50)
	if velocity_x >= 0:
		velx = 1
	else:
		velx = -1

	if velocity_y >= 0.015:
		vely = 1
	elif velocity_y <= -0.015:
		vely = -1
	else:
		vely = 0

	discrete_paddle = floor(12*(paddle_y/(1-120)))
	return (posx, posy, velx, vely, discrete_paddle)


def fixVelocity(velocity):
	vel = velocity
	if velocity >= 0 and velocity < 18:
		vel = 18
	elif velocity < 0 and velocity > -18:
		vel = -18
	return vel