import pygame

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
x_pos = 0
running = True

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
    pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
    x_pos += 1

    # обновление экрана
    pygame.display.flip()
pygame.quit()