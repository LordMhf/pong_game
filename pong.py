import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pong game")
x = 150
y = 450
x_red = 150
y_red = 50

widgh = 150
high = 25

speed = 35
speed1 = 15
x1 = random.randint(100, 400)
y1 = random.randint(100, 400)

x_max = True
y_max = True

score_red = 0
score_blue = 0

run = True
while run:
    pygame.time.delay(100)

    if x1 + speed1 > 500:
        x_max = False
    if x1 - speed1 < 0:
        x_max = True

    if 475 > y1 + speed1 > 450 and x1 in range(x, x + widgh):
        y_max = False
    if 50 < y1 - speed1 < 75 and x1 in range(x_red, x_red + widgh):
        y_max = True

    if y1 > 500:
        score_red += 1
        x1 = random.randint(150, 350)
        y1 = random.randint(150, 350)
    if y1 < 0:
        score_blue += 1
        x1 = random.randint(150, 350)
        y1 = random.randint(150, 350)

    if x_max:
        x1 += speed1
    else:
        x1 -= speed1
    if y_max:
        y1 += speed1
    else:
        y1 -= speed1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x - speed < 0:
            x = 0
        else:
            x -= speed
    if keys[pygame.K_RIGHT]:
        if x + speed > 500 - widgh:
            x = 500 - widgh
        else:
            x += speed

    if keys[pygame.K_a]:
        if x_red - speed < 0:
            x_red = 0
        else:
            x_red -= speed
    if keys[pygame.K_d]:
        if x_red + speed > 500 - widgh:
            x_red = 500 - widgh
        else:
            x_red += speed

    win.fill((0, 0, 0))

    texti = "red score:" + str(score_red) + " _ blue score:" + str(score_blue)
    font = pygame.font.Font(None, 50)
    text = font.render(texti, True, (153, 255, 51))
    win.blit(text, (40, 10))
    pygame.display.flip()

    pygame.draw.circle(win, (255, 255, 255), (x1, y1), 10)
    pygame.draw.rect(win, (0, 0, 255), (x, y, widgh, high))
    pygame.draw.rect(win, (255, 0, 0), (x_red, y_red, widgh, high))

    pygame.display.update()
pygame.quit()
