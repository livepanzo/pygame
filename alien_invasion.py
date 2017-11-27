#-*-coding: utf8-*-
import pygame
from settings import Settings
from ship import Ship
import game_functions  

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height)) 
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        game_functions.check_events(ship)
        game_functions.update_screen(s, screen, ship)
        
        

run_game()