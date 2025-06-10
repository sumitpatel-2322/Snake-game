import pygame
import sys
import random
import pygame.font
pygame.init()
width,height= 600,400
cell_size=20
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
food_x=random.randrange(0,width,cell_size)
food_y=random.randrange(0,height,cell_size)
food=(food_x,food_y)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
snake=[(100,100),(80,100),(60,100)]
direction="RIGHT"
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,48)
score=0
speed=10
def display_score(score):
    score_text=font.render(f"Score: {score}",True,white)
    screen.blit(score_text,(10,10))
def game_over():
    text=font.render("GAME OVER", True, white)
    screen.blit(text,(width//2-100,height//2-25))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()
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
    if (new_head[0]<0 or new_head[0]>=width or
        new_head[1]<0 or new_head[1]>=height):
        game_over()
    if new_head in snake:
        game_over()
    if new_head==food:
        snake.insert(0,new_head)
        score+=1
        speed=min(speed+1,30)
        food=(random.randrange(0,width,cell_size),
              random.randrange(0,height,cell_size))
    else:
        snake=[new_head]+snake[:-1]
    screen.fill(black)
    pygame.draw.rect(screen,red,(*food,cell_size,cell_size))
    for block in snake:
        pygame.draw.rect(screen,green,(*block,cell_size,cell_size))
    display_score(score)
    pygame.display.flip()
    clock.tick(speed)