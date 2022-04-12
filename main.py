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
    #add ship
    ship = Ship(screen)

    aliens = Group()

    #make a group to store bullets
    bullets = Group()

    # draws tha alien fleet
    gf.create_fleet(settings, screen, aliens, ship)

    # loop to start animation
    while True:
        #acess event handler from game_functions
        gf.check_events(ship, settings ,screen,bullets)

        bullets.update()
        #gf.alien_update(aliens)
        #updates screen from g_f
        print(len(aliens))
        gf.update_screen(settings,screen,ship, bullets, aliens)


#runs game
alien_invasion()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
