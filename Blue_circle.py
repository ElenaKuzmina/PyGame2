import pygame
import time

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

running = True

fps = 60
clock = pygame.time.Clock()
screen.fill((0, 0, 0))
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений

    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)

    clock.tick(fps)
    # обновление экрана
    pygame.display.flip()
pygame.quit()