#Samara Sherven 3/29/22

import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
#a class to manage the bullets fired from the ship
#initializes bullets
    def __init__(self,settings,screen,ship):
        #initializes as super of the class Bullets that uses sprites
        super(Bullets,self).__init__()
        self.screen = screen
        #create bullet rectangle
        self.rect = pygame.Rect(0,0,settings.bu_width,settings.bu_height)
        #moves the bullet to the top of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #stores the bullets position as a decimal value
        self.y = float(self.rect.y)
        #sets color and speed of bullets from settings
        self.color = settings.bu_color
        self.speed = settings.bu_speed

    def update(self):
        #sets the speed and updates the position of the bullet
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bu(self):
        #draws bullet as a rectangle using the previous settings
        pygame.draw.rect(self.screen,self.color,self.rect)

