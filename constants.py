__author__ = 'Kim'
import pygame


# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
# Tid
#Play Size
BLOCKS = 15  # Should be an odd number, make a try here later!
BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32
CAPTION_NAME = "Kim's Bomberman"
SCREEN_WIDTH = BLOCKS * BLOCK_WIDTH
SCREEN_HEIGHT = BLOCKS * BLOCK_HEIGHT
#SpriteSheetBlock Width/Height/Margin
SSBW = 16
SSBH = 16
SSM = 1

# 15x15(BLOCKSxBLOCKS) grid der verdiene = 0, ikke i bruk til nå
grid = []
# For hver rekke
# Grid value 1 = hardblock, 2 = softblock, 3 = empty
for row in range(BLOCKS):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(BLOCKS):
        # Add a the number zero to the current row
        grid[row].append(0)


######################################################################

# sprite sheet for map
bomberman_sheet = pygame.image.load("sprite_sheet0.png")
for i in range(4):
    SPRITE_BLOCK_START = 71
    SPRITE_BLOCK_LOWER = 175
    bomberman_sheet.set_clip(pygame.Rect(SPRITE_BLOCK_START + (SSBW+SSM) * i, SPRITE_BLOCK_LOWER, SSBW, SSBH))
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