import pygame
import sys
pygame.init()
width,height= 600,400
cell_size=20
black=(0,0,0)
green=(0,255,0)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
snake=[(100,100),(80,100),(60,100)]
direction="RIGHT"
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!="DOWN":
                direction="UP"
            elif event.key==pygame.K_DOWN and direction!="UP":
                direction="DOWN"
            elif event.key==pygame.K_LEFT and direction!="RIGHT":
                direction="LEFT"
            elif event.key==pygame.K_RIGHT and direction!="LEFT":
                direction="RIGHT"
    head_x,head_y=snake[0]
    if direction=="UP":
        new_head=(head_x,head_y-cell_size)
    elif direction=="DOWN":
        new_head=(head_x,head_y+cell_size)
    elif direction=="LEFT":
        new_head=(head_x-cell_size,head_y)
    elif direction=="RIGHT":
        new_head=(head_x+cell_size,head_y)
    snake=[new_head]+snake[:-1]
    screen.fill(black)
    for block in snake:
        pygame.draw.rect(screen,green,(*block,cell_size,cell_size))
    pygame.display.flip()
    clock.tick(20)