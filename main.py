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

#Play Size
BLOCKS = 15
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




# 15x15(BLOCKSxBLOCKS) grid der verdiene = 0
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


all_sprites_list = pygame.sprite.Group()

unmovable_object = HardBlock()
all_sprites_list.add(unmovable_object)

# Set positions of graphics
background_position = [0, 0]
# block_position = (71,175,16,16)







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
            print("Click")





    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    mouse_position = pygame.mouse.get_pos()
    unmovable_object.rect.x = mouse_position[0]
    unmovable_object.rect.y = mouse_position[1]

    # Copy image to screen:

    for column in range(BLOCKS):
        column_area = 0 < column < BLOCKS-1
        row_area = 0 < row < BLOCKS-1

        for row in range(BLOCKS):
            if not column_area:
                screen.blit(hard_block2x, [column*BLOCK_WIDTH,row*BLOCK_HEIGHT])
            elif row == 0 and column_area or row == BLOCKS-1 and column_area:
                screen.blit(hard_block2x, [column*BLOCK_WIDTH,row*BLOCK_HEIGHT])
            elif column == 1 and row_area :
                screen.blit(field_shadow2x, [row*BLOCK_WIDTH,column*BLOCK_HEIGHT])
            else:
                screen.blit(field2x, [row*BLOCK_WIDTH,column*BLOCK_HEIGHT])
        for row in range(2, BLOCKS-1, 2):
            if not (column % 2) and column_area:
                screen.blit(hard_block2x, [row*BLOCK_WIDTH,column*BLOCK_HEIGHT])
            elif (column % 2) and column_area :
                screen.blit(field_shadow2x, [row*BLOCK_WIDTH,column*BLOCK_HEIGHT])

    all_sprites_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)


pygame.quit ()