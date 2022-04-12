#Samara Sherven 3/29/22

import pygame

class Ship():
    def __init__(self, screen):
        '''initialize ship and starting position'''
        #load ship image as a rectangle
        self.image = pygame.image.load('images/user_rocket.png')
        self.image = pygame.transform.scale(self.image, (30,40))
        self.rect = self.image.get_rect()
        #calls the screen as a rectangle
        self.screen_rect = screen.get_rect()
        self.screen = screen

        #sets the ship to the center, top, and bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #stores center x&y of ship as decimal
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        #creates movement flag that determines if moving, set to false
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        '''draw ship @ current location'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        """updates image of ship left/right and creates boundaries it cannot cross"""
        if self.moving_right and self.rect.centerx < 1072:
            self.center += 1.0
        elif self.moving_left and self.rect.centerx > 25:
            self.center -= 1.0

        elif self.moving_up and self.rect.top > 350:
            self.center2 -= 1.0
        elif self.moving_down and self.rect.top < 555:
            self.center2 += 1.0
        #sets and updated the x&y
        self.rect.centerx = self.center
        self.rect.centery = self.center2
