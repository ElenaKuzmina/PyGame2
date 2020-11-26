import pygame
import random


def draw():
    for i  in range(10000):
        screen.fill(pygame.Color('white'), (random.random() * width,
                                            random.random() * height, 1, 1))

size = width, height = 301, 301
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    draw()
    pygame.display.flip()

pygame.quit()