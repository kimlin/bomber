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
import random

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Play Size
BLOCKS = 15  # Should be an odd number, make a try here later!
BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32
CAPTION_NAME = "Kim's Bomberman"
SCREEN_WIDTH = BLOCKS * BLOCK_WIDTH
SCREEN_HEIGHT = BLOCKS * BLOCK_HEIGHT
#SpriteSheet
SPRITE_SHEET0_BLOCK_WIDTH = 16
SPRITE_SHEET0_BLOCK_HEIGHT = 16
#Buildingblocks Sprites
SPRITE_BLOCK_START = 71
SPRITE_BLOCK_LOWER = 175
SPRITE_MARGIN = 1

# sprite sheet



bomberman_sheet = pygame.image.load("sprite_sheet0.png")
for i in range(4):
    bomberman_sheet.set_clip(pygame.Rect(SPRITE_BLOCK_START + (SPRITE_SHEET0_BLOCK_WIDTH+SPRITE_MARGIN) * i, SPRITE_BLOCK_LOWER, SPRITE_SHEET0_BLOCK_WIDTH, SPRITE_SHEET0_BLOCK_HEIGHT))
    if i == 0:
        hard_block = bomberman_sheet.subsurface(bomberman_sheet.get_clip())
        hard_block2x = pygame.transform.scale2x(hard_block)
    elif i == 1:
        soft_block = bomberman_sheet.subsurface(bomberman_sheet.get_clip())
        soft_block2x = pygame.transform.scale2x(soft_block)
    elif i == 2:
        field_shadow = bomberman_sheet.subsurface(bomberman_sheet.get_clip())
        field_shadow2x = pygame.transform.scale2x(field_shadow)
    elif i == 3:
        field = bomberman_sheet.subsurface(bomberman_sheet.get_clip())
        field2x = pygame.transform.scale2x(field)



class HardBlock(pygame.sprite.Sprite):

    def __init__(self):

    # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load the image
        self.image = hard_block2x

        # Set our transparent color
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

class SoftBlock(pygame.sprite.Sprite):

    def __init__(self):

    # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load the image
        self.image = soft_block2x

        # Set our transparent color
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()




# 15x15(BLOCKSxBLOCKS) grid der verdiene = 0, ikke i bruk til nå
grid = []
# For hver rekke
for row in range(BLOCKS):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(BLOCKS):
        # Add a the number zero to the current row
        grid[row].append(0)


# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# This sets the name of the window
pygame.display.set_caption(CAPTION_NAME)
clock = pygame.time.Clock()

# all_sprite_list
all_sprites_list = pygame.sprite.Group()
# heavy sprite blocks
hardblock_list = pygame.sprite.Group()
unmovable_object = HardBlock()


for column in range(BLOCKS):

    for row in range(BLOCKS):
        # This represents a hardblock
        hardblock = HardBlock()
        column_area = 0 < column < BLOCKS-1
        if not column_area:
            # Set a random location for the block
            hardblock.rect.x = column * BLOCK_HEIGHT
            hardblock.rect.y = row * BLOCK_WIDTH
            # Add the block to the list of objects
            all_sprites_list.add(hardblock)
            hardblock_list.add(hardblock)
            grid[row][column] = 1
        elif row == 0 and column_area or row == BLOCKS-1 and column_area:
            hardblock.rect.x = column * BLOCK_HEIGHT
            hardblock.rect.y = row * BLOCK_WIDTH
            all_sprites_list.add(hardblock)
            hardblock_list.add(hardblock)
            grid[row][column] = 1
    for row in range(2, BLOCKS-1, 2):
        hardblock = HardBlock()
        column_area = 0 < column < BLOCKS-1
        if not (column % 2) and column_area:
            hardblock.rect.x = column * BLOCK_HEIGHT
            hardblock.rect.y = row * BLOCK_WIDTH
            all_sprites_list.add(hardblock)
            hardblock_list.add(hardblock)
            grid[row][column] = 1

# soft sprite blocks loads after hardblocks
softblock_list = pygame.sprite.Group()
movable_object = SoftBlock()


for column in range(BLOCKS):

    for row in range(BLOCKS):
        # This represents a hardblock
        softblock = SoftBlock()
        column_area = 0 < column < BLOCKS-1
        if 2 < row < 14 and BLOCKS-row > 3:
            if grid[row][column] == 0:
                softblock.rect.x = column * BLOCK_HEIGHT
                softblock.rect.y = row * BLOCK_WIDTH
                all_sprites_list.add(softblock)
                softblock_list.add(softblock)
        elif 2 < column < 14 and BLOCKS-column > 3:
            if grid[row][column] == 0:
                softblock.rect.x = column * BLOCK_HEIGHT
                softblock.rect.y = row * BLOCK_WIDTH
                all_sprites_list.add(softblock)
                softblock_list.add(softblock)

'''
softblock.rect.x = column * BLOCK_HEIGHT
softblock.rect.y = row * BLOCK_WIDTH
all_sprites_list.add(softblock)
softblock_list.add(softblock)
'''

# Set positions of graphics
background_position = [0, 0]
# block_position = (71,175,16,16)





# Load and set up graphics.
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            column = mouse_position[0] // BLOCK_WIDTH
            row = mouse_position[1] // BLOCK_HEIGHT
            print(row)
            print(column)
            print("Heavy block = ", grid[row][column])


    mouse_position = pygame.mouse.get_pos()


    '''
    mouse_position = pygame.mouse.get_pos()
    unmovable_object.rect.x = mouse_position[0]
    unmovable_object.rect.y = mouse_position[1]
    '''
    # Copy image to screen:

    for column in range(BLOCKS):
        column_area = 0 < column < BLOCKS-1
        row_area = 0 < row < BLOCKS-1

        for row in range(BLOCKS):
            if column == 1 and row_area :
                screen.blit(field_shadow2x, [row*BLOCK_WIDTH,column*BLOCK_HEIGHT])
            else:
                screen.blit(field2x, [row*BLOCK_WIDTH,column*BLOCK_HEIGHT])

        for row in range(2, BLOCKS-1, 2):
            if (column % 2) and column_area :
                screen.blit(field_shadow2x, [row*BLOCK_WIDTH,column*BLOCK_HEIGHT])

    all_sprites_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)


pygame.quit ()