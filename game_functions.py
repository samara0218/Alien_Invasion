#Samara Sherven 3/29/22

import pygame
import sys

from bullets import Bullets
from alien import Alien

def check_events(ship, settings,screen,bullets):
    """checks for key/mouse events and responds"""
    #loop to check keypress events
    for event in pygame.event.get():
        #if esc key pressed, exit game
        if event.type == pygame.QUIT:
            sys.exit()
        #Checks if a key is pressed
        elif event.type == pygame.KEYDOWN:
            keydown_evt(event,settings, screen, bullets,ship)
        #checks if a key is not pressed
        elif event.type == pygame.KEYUP:
            keyup_evt(event,ship)

def create_fleet(settings,screen,aliens,ship):
    """create a fleet of aliens"""
    alien = Alien(settings,screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings,alien.rect.height, ship.rect.height)

    print(number_of_aliens * number_of_rows)

    print(number_of_rows)
    print(number_of_aliens)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)



def get_number_of_aliens(settings,alien_width):
    """determine the num of aliens that fit in a row"""
    available_space_x = settings.screenWidth - 2 * alien_width
    number_of_aliens  = int(available_space_x / (2 * alien_width))
    return number_of_aliens

def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screenHeight - 6 * alien_height - ship_height
    number_of_rows = int(available_space_y / (2.5 * alien_height))
    return number_of_rows

def number_of_aliens(settings, alien_height, alien_width, ship_height):
    number_of_actual_aliens = get_number_rows(settings, alien_height, ship_height) * get_number_of_aliens(settings, alien_width)
    return number_of_actual_aliens

def create_alien(settings,screen, aliens, alien_number, row_number):
    """create an alien and place it on a row"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = float(2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)

def check_fleet(aliens,settings):
    if len(aliens) == 0:
        #settings.score += 20
        settings.fleet_lim += 1

        return True
    else:
        return False

def game_end(settings):
    if settings.fleet_lim == 3:
        print("You are superior congrats")
        print("Your score was " + str(settings.score))
        return True
    elif settings.lives == 0:
        print("You died lol imagine")
        print("Your score was " + str(settings.score))
        return True
    else:
        return False

def close_game(settings):
    if game_end(settings) == True:
        sys.exit()

def check_collision(bullets,aliens, settings):
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        settings.score += 1

def check_ship(ship, settings, aliens):
    for alien in aliens:
        if alien.rect.bottomleft == ship.rect.topleft:
            for alien in aliens:
                alien.kill()
            settings.lives -= 1
            #settings.score -= 20
            return True

def print_text(settings,screen):
    surface = settings.font.render("Score: " + str(settings.score), True, (0,255,0))
    screen.blit(surface, (50,540))
    surface2 = settings.font.render("Lives: " + str(settings.lives), True, (0, 255, 0))
    screen.blit(surface2, (50, 565))
    #surface3 = settings.font.render("Iteration: " + str(settings.fleet_lim), True, (0, 255, 0))
    #screen.blit(surface3, (50, 515))

def update_screen(settings,screen,ship, bullets, alien):
    #color the screen with bg color
    check_ship(ship,settings,alien)
    screen.fill(settings.bg_color)
    # draw bullet
    #check_ship(ship,alien,settings)
    for bullet in bullets.sprites():
        bullet.draw_bu()
        bullet.update()

    if (check_fleet(alien,settings) == True or check_ship(ship,settings,alien) == True) and game_end(settings) == False:
        create_fleet(settings,screen,alien,ship)

    alien.draw(screen)
    # draw alien fleet
    alien.update()

    #update ship
    ship.update()
    #draw ship
    ship.blitme()

    check_collision(bullets,alien, settings)
    print_text(settings, screen)
    #update display
    pygame.display.flip()



def keydown_evt(event, settings, screen, bullets, ship):
    #if lef, right, up, down are pressed the ship moving flag is set to true
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    #if the space bar is pressed a new bullet is created and added to the group
    if event.key == pygame.K_SPACE:
        if len(bullets) <= settings.bu_limit:
            new_bu = Bullets(settings,screen,ship)
            bullets.add(new_bu)

def keyup_evt(event,ship):
    # if a key is not pressed the moving flag is set to false
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False




