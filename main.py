import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((500, 750))  
BACKGROUND_IMAGE = pygame.image.load('background23.jpg')
BIRD_IMAGE = pygame.image.load('bird.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))

OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 253, 117)
OBSTACE_X_CHANGE = -1
obstacle_x = 500

GAP = 150  
score = 0 
if obstacle_x <= -OBSTACLE_WIDTH:
    obstacle_x = 500
    OBSTACLE_HEIGHT = random.randint(50, 400) 
    score += 1

def display_obstacle(height):
    bottom_obstacle_height = 635 - height - GAP
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, height + GAP, OBSTACLE_WIDTH, bottom_obstacle_height))



def collision_detection (obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False


score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    SCREEN.blit(display, (10, 10))


startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
   
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    SCREEN.blit(display, (20, 200))
    pygame.display.update()

score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def game_over():
    maximum = max(score_list)
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    SCREEN.blit(display1, (50, 300))
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200,35,35))
        SCREEN.blit(display3, (80, 100))

running = True
waiting = True
collision = False

clock = pygame.time.Clock()

while running:

    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    while waiting:
        if collision:
            game_over()
            start()
        else:           
            start()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    bird_y = 300
                    obstacle_x = 500
                    
                    waiting = False

            if event.type == pygame.QUIT:
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               
                bird_y_change = -6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                
                bird_y_change = 3

   
    bird_y += bird_y_change
    
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 571:
        bird_y = 571

    
    obstacle_x += OBSTACE_X_CHANGE

   
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 150)

    if collision:
        score_list.append(score)
        waiting = True

   
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1
        print("Score:", score)  
 
    display_obstacle(OBSTACLE_HEIGHT)

    
    display_bird(bird_x, bird_y)

   
    score_display(score)

    
    pygame.display.update()
    
    clock.tick(60)


pygame.quit()