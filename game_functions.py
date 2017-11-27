#-*-coding: utf8-*-
import sys
import pygame 


def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши."""

    for event in pygame.event.get():
        # print(pygame.event.event_name(event.type))
        # print(pygame.event.get_blocked(event.type))
        # print(event.dict)
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == 'keydown':
        #     print(event.type)
        #     if event.key == K_RIGHT:
        #         ship.rect.centerx += 30
        #         print(ship.rect.centerx)
        # все кнопки сохранены как pygame.CONSTANTA 
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                ship.rect.centerx += 30
            elif event.key == pygame.K_LEFT :
                ship.rect.centerx -= 30

def update_screen(s, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(s.bg_color)
    ship.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()