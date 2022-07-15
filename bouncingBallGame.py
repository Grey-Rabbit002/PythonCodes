import pygame
import sys
pygame.init()

size = width, height =1000, 750
speed = [1, 1]
background = 255, 255, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")

#get_rect()
#Returns a new rectangle covering the entire surface.
#This rectangle will always start at (0, 0) with a width and height
#the same size as the image.
#You can pass keyword argument values to this function.

ball = pygame.image.load("C:/Users/Arjun/Downloads/jupi.png")
ballrect = ball.get_rect()
#Pygame will register all events from the user into an event queue
#which can be received with the code pygame.event.get().
#Every element in this queue is an Event object and they'll all
#have the attribute type, which is an integer representing what kind of event
#it is.
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()
