# Samara Sherven 3/29/22

import pygame
from settings import Settings
from pygame.sprite import Sprite

class Alien(Sprite):
#a class to represent 1 alien in the fleet
#initializes aliens
    def __init__(self,settings,screen):
        #initializes as super of the class Aliens that uses sprites
        super(Alien,self).__init__()
        self.screen = screen
        self.settings = settings

        #create alien image (from pixabay.com) as rectangle
        self.image = pygame.image.load('images/mario_PNG.png')
        #scales the alien
        self.image = pygame.transform.scale(self.image, (45, 35))
        # makes image a square
        self.rect = self.image.get_rect()
        #creates starting position of the alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.left = self.rect.left
        self.rect.right = self.rect.right
        self.rect.top = self.rect.top

        self.top = float(self.rect.top)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # spacing for fleet
        self.available_space_x = 1100 - (2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2 * self.rect.width))

        self.speed = 1
        self.direction = 1

        self.alien_right = True
        self.alien_left = False



    def blitme(self):
        '''draw alien @ current location'''
        self.screen.blit(self.image,self.rect)


    def check_screen(self):
        """return True id an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= -1:
            return True

    def update(self):
        """moves alien"""
        self.rect.x = float(self.rect.x + self.speed)
        if self.rect.left < 0 or self.rect.right > 1100:
            self.speed = -self.speed
            self.rect.y += 35

#function to move the aliens back and forth



    #function to get rid of alien if hit

    #function that checks if there is another alien in front

    #using previous function if true then shoot

    #function for alien bullets

