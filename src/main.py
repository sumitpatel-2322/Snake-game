import pygame
import sys
import random
import os
pygame.init()
width,height= 600,400
cell_size=20
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
highscore_file="highscore.txt"
if os.path.exists(highscore_file):
    with open (highscore_file,"r")as f:
        highscore=int(f.read().strip() or 0)
else:
    highscore=0
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,48)

def display_score(score,highscore):
    score_text=font.render(f"Score: {score}",True,white)
    highscore_text=font.render(f"High Score: {highscore}",True,white)
    screen.blit(score_text,(10,10))
    screen.blit(highscore_text,(10,40))
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen,green,(*block,cell_size,cell_size))
def draw_food(food):
    pygame.draw.rect(screen,red,(*food,cell_size,cell_size))
def save_highscore(score):
    global highscore
    if score>highscore:
        highscore=score
        with open (highscore_file,"w") as f:
            f.write(str(highscore))
def show_game_over(score):
    save_highscore(score)
    screen.fill(black)
    game_over_text=font.render("GAME OVER",True,white)
    restart_text=font.render("Press R to Restart or Q to Quit",True,white)
    final_score_text=font.render(f"Your Score: {score}",True,white)
    screen.blit(game_over_text,(width//2-80,height//2-60))
    screen.blit(final_score_text,(width//2-90,height//2-20))
    screen.blit(restart_text,(width//2-220,height//2+20))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
def main():
    global highscore
    snake=[(100,100),(80,100),(60,100)]
    direction="RIGHT"
    food_x=random.randrange(0,width,cell_size)
    food_y=random.randrange(0,height,cell_size)
    food=(food_x,food_y)
    score=0
    speed=10
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
            new_head[1]<0 or new_head[1]>=height or new_head in snake):
            show_game_over(score)
        if new_head==food:
            snake.insert(0,new_head)
            score+=1
            speed=min(speed+1,30)
            food=(random.randrange(0,width,cell_size),
                random.randrange(0,height,cell_size))
        else:
            snake=[new_head]+snake[:-1]
        screen.fill(black)
        draw_food(food)
        draw_snake(snake)
        display_score(score,highscore)
        pygame.display.flip()
        clock.tick(speed)

# def game_over():
#     text=font.render("GAME OVER", True, white)
#     screen.blit(text,(width//2-100,height//2-25))
#     pygame.display.flip()
#     pygame.time.delay(2000)
#     pygame.quit()
#     sys.exit()
main()