import pygame as pg
import os
import random

pg.init()
# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
screen = pg.display.set_mode((398, 360))
bg_image = pg.image.load(os.path.join(img_folder, 'arrow.png')).convert()


# Player settings
BELL_IMAGE = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
bell_x = 75
bell_y = 200
bell_y_change = 0
# Image of player is displayed on the screenw with coordinates 
def player_bell(x, y):
    screen.blit(BELL_IMAGE, (x, y))

# Platform settings 
PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = random.randint(150, 310)
PLATFORM_COLOR = (200, 175, 200)
PLATFORM_X_CHANGE = - 0.05
platform_x = 360
# Shows platform on the screen with randomized height but same area everytime
def platform_rect(height):
    pg.draw.rect(screen, PLATFORM_COLOR, (platform_x, 0, PLATFORM_WIDTH, height))
    bottom_platform_height = 360 - height - 150
    pg.draw.rect(screen, PLATFORM_COLOR, (platform_x, 398, PLATFORM_WIDTH, -bottom_platform_height))

# Collision detection between the player and the platform
def collision_detection (platform_x, platform_height, bell_y, bottom_platform_height):
     if platform_x >= 75 and platform_x <= (50 + 50):
          if bell_y <= platform_height or bell_y >= (bottom_platform_height - 35):
               return True
          return False

# Game Loop    
running = True 
while running:
# screen becomes Black 
    screen.fill((0, 0, 0))
# Background image shows up on the screen
    screen.blit(bg_image, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
 # controls for the gam when any letter is pressed   
        if event.type == pg.KEYDOWN:
                bell_y_change = -0.09
        if event.type == pg.KEYUP:
                bell_y_change = 0.06
        
 # Stops player from going vertically out of the screen
    bell_y += bell_y_change
    if bell_y <= 0:
         bell_y = 0
    if bell_y >= 328:
        bell_y = 328
    player_bell(bell_x, bell_y)

#Moves the platform to the left and once hits -10 it goes back to starting position with a random height
    platform_x += PLATFORM_X_CHANGE
    if platform_x <= -10:
         platform_x = 398
         PLATFORM_HEIGHT = random.randint(100, 310)
    platform_rect(PLATFORM_HEIGHT)

# collision function and what I want to collide
    collision = collision_detection(platform_x, PLATFORM_HEIGHT, bell_y, PLATFORM_HEIGHT + 150)
# Game stops running if hit
    if collision:
        pg.quit()

# Updates the display on the screen   
    pg.display.update()
# Window closes 
pg.quit()