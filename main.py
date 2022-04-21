#Samara Sherven 3/29/22

import pygame
import sys

import alien
from settings import Settings
import game_functions as gf
from ship import Ship
from pygame.sprite import Group
from alien import Alien

# function called to run the game


def alien_invasion():
    #initializes pygame and settings
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption('Alien Invasion')
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)

    #add ship
    ship = Ship(screen)

    aliens = Group()

    #make a group to store bullets
    bullets = Group()

    text = font.render('score is: ' + str(settings.score), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (80 // 2, 100 // 2)

    # draws tha alien fleet
    gf.create_fleet(settings, screen, aliens, ship)

    # loop to start animation
    while True:
        #acess event handler from game_functions
        gf.check_events(ship, settings ,screen,bullets)

        #print(len(aliens))
        #print(len(bullets))
        gf.update_screen(settings,screen,ship, bullets, aliens)
        gf.close_game(settings)
        screen.blit(text, textRect)


#runs game
alien_invasion()
print(Settings.score)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
