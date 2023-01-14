# General
import pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Properties
width, height = 1280, 960
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")
font = pygame.font.SysFont("sourcesans", 50)
font1 = pygame.font.SysFont("monospace", 50)
font2 = pygame.font.SysFont("sourcesans", 25)
font3 = pygame.font.SysFont("monospace", 25)

# Rects
ball = pygame.Rect(width/2-15, height/2-15,30,30)
player1 = pygame.Rect(width-20,height/2-70,10,140)
player2 = pygame.Rect(10, height/2 - 70, 10, 140)

speed = 10
ball_speed_x = speed-3
ball_speed_y = speed-3
player1paddle = 0
player2paddle = 0
score = 0
highest_score = 0

def restart():
    ball.center = (width/2, height/2)
    global score, ball_speed_x, ball_speed_y
    score = 0
    speed = 10
    ball_speed_x = speed-3
    ball_speed_y = speed-3


while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1paddle += speed
            if event.key == pygame.K_UP:
                player1paddle -= speed
            if event.key == pygame.K_w:
                player2paddle -= speed
            if event.key == pygame.K_s:
                player2paddle += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1paddle -= speed
            if event.key == pygame.K_UP:
                player1paddle += speed
            if event.key == pygame.K_w:
                player2paddle += speed
            if event.key == pygame.K_s:
                player2paddle -= speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    player1.y += player1paddle
    player2.y += player2paddle

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= height:
        player1.bottom = height
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= height:
        player2.bottom = height

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        restart()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        score+=1
        if score % 10 == 0:
            speed+=0.5
        if highest_score < score:
            highest_score = score

    # Visuals
    screen.fill((231, 235, 224))
    pygame.draw.rect(screen, (249,161,46), player1)
    pygame.draw.rect(screen, (154,74,151), player2)
    pygame.draw.ellipse(screen, (252,118,106), ball)
    pygame.draw.aaline(screen, (250,250,250), (width/2,0), (width/2, height))

    text = font.render("SCORE", True, (200,200,200))
    text_rect = text.get_rect(center=(width/2, 25))
    screen.blit(text, text_rect)

    text1 = font1.render(str(score), True, (200, 200, 200))
    text1_rect = text1.get_rect(center=(width/2, 60))
    screen.blit(text1, text1_rect)

    text2 = font2.render("HIGHEST SCORE", True, (200,200,200))
    text2_rect = text2.get_rect(center=(width/2, 95))
    screen.blit(text2, text2_rect)

    text3 = font3.render(str(highest_score), True, (200, 200, 200))
    text3_rect = text3.get_rect(center=(width / 2, 115))
    screen.blit(text3, text3_rect)


    # Update sys
    pygame.display.flip()
    clock.tick(60)
