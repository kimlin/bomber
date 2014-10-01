__author__ = 'Kim'
"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/4YqIKncMJNs
 Explanation video: http://youtu.be/ONAK8VZIcI4
 Explanation video: http://youtu.be/_6c4o41BIms
"""

import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
CAPTION_NAME = "Kim's Bomberman"

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# This sets the name of the window
pygame.display.set_caption(CAPTION_NAME)

clock = pygame.time.Clock()

# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("laser5.ogg")

# Set positions of graphics
background_position = [0, 0]
# block_position = (71,175,16,16)

# sprite sheet

SPRT_RECT_X = 71
SPRT_RECT_Y = 175
LEN_SPRT_X = 16
LEN_SPRT_Y = 16
bomberman_sheet = pygame.image.load("sprite_sheet0.png")
bomberman_sheet.set_clip(pygame.Rect(SPRT_RECT_X, SPRT_RECT_Y, LEN_SPRT_X, LEN_SPRT_Y))
hard_block = bomberman_sheet.subsurface(bomberman_sheet.get_clip())
hard_block2x = pygame.transform.scale2x(hard_block)

# Load and set up graphics.
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    # Copy image to screen:
    screen.blit(background_image, background_position)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # Copy image to screen:
    screen.blit(player_image, [x, y])
    screen.blit(hard_block, [0,0])
    screen.blit(hard_block2x, [16,16])

    pygame.display.flip()

    clock.tick(60)


pygame.quit ()