import pygame
import random


def createBullet():
    bullet_rect = bullet.get_rect()
    bullet_rect.center = ship_rect.midtop
    bullet_list.append(bullet_rect)


def moveBullets():
    for i in range(len(bullet_list)):
        bullet_list[i].move_ip(0, -5)


def createEnemy():
    enemy_rect.center = (random.randint(0, width), 0)


def moveEnemies():
    enemy_rect.move_ip(0, 3)


def removeEnemy():
    for bullet_rect in bullet_list:
        if enemy_rect.colliderect(bullet_rect):
            bullet_list.remove(bullet_rect)
            createEnemy()
            return

    if enemy_rect.top > height:
        createEnemy()


def drawScreen():
    screen.blit(background, (0, 0))
    screen.blit(spaceship, ship_rect)
    screen.blit(enemy, enemy_rect)
    for bullet_rect in bullet_list:
        screen.blit(bullet, bullet_rect)
    pygame.display.flip()
    clock.tick(60)


pygame.init()

width, height = 400, 600
size = (width, height)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

background = pygame.image.load('images\\background.jpeg').convert()
background = pygame.transform.scale(background, size)

spaceship = pygame.image.load('images\\spaceship.png')
ship_rect = spaceship.get_rect()
ship_rect.center = (200, 550)

enemy = pygame.image.load('images\\enemy1.png')
enemy_rect = enemy.get_rect()
createEnemy()

bullet = pygame.image.load('images\\bullet.png')
bullet_list = []

ship_dx, ship_dy = 0, 0
speed = 2
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_dx -= speed
            elif event.key == pygame.K_RIGHT:
                ship_dx += speed
            elif event.key == pygame.K_UP:
                ship_dy -= speed
            elif event.key == pygame.K_DOWN:
                ship_dy += speed
            elif event.key == pygame.K_SPACE:
                createBullet()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship_dx += speed
            elif event.key == pygame.K_RIGHT:
                ship_dx -= speed
            elif event.key == pygame.K_UP:
                ship_dy += speed
            elif event.key == pygame.K_DOWN:
                ship_dy -= speed

    ship_rect = ship_rect.move(ship_dx, ship_dy)
    moveEnemies()
    moveBullets()
    removeEnemy()
    drawScreen()