#Samara Sherven 3/29/22

class Settings():
# Class to store all settings for Alien Invasion
    def __init__(self):
        #initializing game settings
        self.screenWidth = 1100
        self.screenHeight = 600
        self.bg_color = (50,50,50)

    #bullet settings
        self.bu_speed = 1
        self.bu_width = 3
        self.bu_height = 10
        self.bu_color = (255,255,255)
    #player settings
        self.lives = 3
        self.score = 0



