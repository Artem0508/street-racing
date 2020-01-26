import pygame
import random
from pygame.transform import scale

class my_car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 100)
        self.image = scale(pygame.image.load("my_car.png"), (150, 200))
        self.xvel = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, left, right, cars):
        if left:
            self.xvel += -3

        if right:
            self.xvel += 3

        if not (left or right):
            self.xvel = 0

        for car in cars:
            if self.rect.colliderect(car.rect):
                rx = random.randint(-5, 40)
                ry = random.randint(-5, 40)

        self.rect.x += self.xvel

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = scale(pygame.image.load("car1.png"), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.yvel

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Street racing")
timer = pygame.time.Clock()

road = scale(pygame.image.load("road.png"), (1280, 1024))
m_car = my_car(400, 400)

left = False
right = False

cars = []

pygame.font.init()

while True:

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right = True

        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right = False

        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")

    screen.blit(road, (0, 0))

    m_car.update(left, right, cars)
    m_car.draw(screen)

    pygame.display.update()
