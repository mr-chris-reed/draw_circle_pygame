# imports
import pygame, sys
from pygame.locals import *

# initializing pygame, setting up surface (canvas)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Shapes")

# drawing some shapes
pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (200, 150), 50)

# game loop - poll events until window is closed out
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
    pygame.display.update()