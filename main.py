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

BLOCKS = 15
BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32
CAPTION_NAME = "Kim's Bomberman"
SCREEN_WIDTH = BLOCKS * BLOCK_WIDTH
SCREEN_HEIGHT = BLOCKS * BLOCK_HEIGHT
SPRITE_SHEET0_BLOCK_WIDTH = 16
SPRITE_SHEET0_BLOCK_HEIGHT = 16

# 15x15(BLOCKSxBLOCKS) grid der verdiene = 0
hard_block_grid = []
# For hver rekke
for row in range(BLOCKS):
    # For each row, create a list that will
    # represent an entire row
    hard_block_grid.append([])
    # Loop for each column
    for column in range(BLOCKS):
        # Add a the number zero to the current row
        hard_block_grid[row].append(0)


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
LEN_SPRT_X = SPRITE_SHEET0_BLOCK_WIDTH
LEN_SPRT_Y = SPRITE_SHEET0_BLOCK_HEIGHT
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
    screen.blit(hard_block2x, [0,0])
    for column in range(BLOCKS):
        for row in range(BLOCKS):
            if column == 0 or column == BLOCKS-1:
                screen.blit(hard_block2x, [column*BLOCK_WIDTH,row*BLOCK_HEIGHT])
            elif row == 0 or row == BLOCKS-1:
                screen.blit(hard_block2x, [column*BLOCK_WIDTH,row*BLOCK_HEIGHT])
        for row in range(0, BLOCKS-1, 2):
            if not (column % 2):
                screen.blit(hard_block2x, [column*BLOCK_WIDTH,row*BLOCK_HEIGHT])
    pygame.display.flip()

    clock.tick(60)


pygame.quit ()