import pygame
import time

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
x_pos = 0
y_pos = 0
running = True
v = 50  # пикселей в секунду, скорость движения
fps = 60
clock = pygame.time.Clock()

while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    # ...
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 250), 20)
    x_pos += v / fps
    clock.tick(fps)

    # обновление экрана
    pygame.display.flip()
pygame.quit()