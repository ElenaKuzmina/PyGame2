import pygame

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Желтый круг")
    size = w, h = 600, 600
    scr = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    run = True
    drawing = False
    scr.fill((0, 0, 255))
    pygame.display.flip()
    d = 0
    # Каждые 100 мс будет выполняться мое событие (1сек = 1000 мс)
    pygame.time.set_timer(pygame.USEREVENT + 1, 100)
    # Для проверки таймера - 1сек
    # pygame.time.set_timer(pygame.USEREVENT + 2, 1000)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                scr.fill((0, 0, 255))
                d = 0
                x, y = event.pos
                drawing = True
            if event.type == pygame.USEREVENT + 1 and drawing:
                d += 1  # т.е. за 1 сек. радиус увеличиться на 10px
                pygame.draw.circle(scr, 'yellow', (x, y), int(d))
                pygame.display.flip()
            # if event.type == pygame.USEREVENT + 2:
            #     print(d)
        clock.tick(30)
    pygame.quit()
