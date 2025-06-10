import pygame
import sys
pygame.init()
width,height= 600,400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    pygame.display.flip()