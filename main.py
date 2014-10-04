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

##########################CONSTANTS##################################
#Skal legges i egen fil senere
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

#Play Size
BLOCKS = 17  # Should be an odd number, make a try here later!
BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32
CAPTION_NAME = "Kim's Bomberman"
SCREEN_WIDTH = BLOCKS * BLOCK_WIDTH
SCREEN_HEIGHT = BLOCKS * BLOCK_HEIGHT
#SpriteSheetBlock Width/Height/Margin
SSBW = 16
SSBH = 16
SSM = 1
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


class Hitbox(pygame.sprite.Sprite):

    direction = "D"
    movement_x = 0
    movement_y = 0
    walls = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.rect = pygame.Rect(player.rect.x + 8,player.rect.y + 34, 18 ,14)

        self.image = pygame.Surface([22, 14])
        self.image.fill(WHITE)
        self.rect = pygame.Rect(BLOCK_WIDTH + 6,BLOCK_HEIGHT + 34, 22 ,14)
        '''
        self.rect.y = 34
        self.rect.x = 8
        '''


    def update(self):
        self.rect.x += self.movement_x
        #print(self.rect.bottom)
        print(self.movement_y)

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.movement_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # Move up/down
        self.rect.y += self.movement_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.movement_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    def go_down(self):
        self.movement_y = 2
        self.direction = "D"
    def go_left(self):
        self.movement_x = -1.5
        self.direction = "L"
    def go_right(self):
        self.movement_x = 2
        self.direction = "R"
    def go_up(self):
        self.movement_y = -1.5
        self.direction = "U"

    def stop_x(self):
        self.movement_x = 0
        self.rect.x += self.movement_x
    def stop_y(self):
        self.movement_y = 0
        self.rect.y += self.movement_y

#####################################################################################
############################## player with sprite sheet:#############################
##################################Skal i egen fil ###################################
class Player(pygame.sprite.Sprite):

    # vi setter startverdiene til Player:
    movement_x = 0
    movement_y = 0

    # Liste med de forskjellige bevegelses bildene, listen er tom nå:
    walking_frames_d = []
    walking_frames_u = []
    walking_frames_l = []
    walking_frames_r = []

    # Hvilken vei ser spilleren når han starter? D= down
    direction = "D"
    # my_collide_rect = lambda a, b: a.hitbox.colliderect(b.hitbox)


    # Metoder
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        i = 0
        sheet_start_x = 51
        sheet_start_y = 38
        frame_width = 17
        frame_height = 24
        sheet_margin = 1
        sprite_sheet = pygame.image.load("sprite_sheet0.png")
        # nå laster vi inn alle bildene der bomberman går nedover:
        for i in range(0, 3):
            sprite_sheet.set_clip(sheet_start_x + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
            frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            frame.set_colorkey(GRAY)
            frame2x = pygame.transform.scale2x(frame)
            frame2x.set_colorkey(GRAY)
            self.walking_frames_d.append(frame2x)
            # vi kan ikke gå 0,1,2,0,1,2 vi må gå 0,1,2,1,0,1,2
            if i == 2:
                i= 1
                sprite_sheet.set_clip(sheet_start_x + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
                frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
                frame.set_colorkey(GRAY)
                frame2x = pygame.transform.scale2x(frame)
                self.walking_frames_d.append(frame2x)
        for i in range(3, 6):
            sprite_sheet.set_clip(sheet_start_x + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
            frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            frame.set_colorkey(GRAY)
            frame2x = pygame.transform.scale2x(frame)
            self.walking_frames_l.append(frame2x)
            # vi kan ikke gå 0,1,2,0,1,2 vi må gå 0,1,2,1,0,1,2
            if i == 5:
                i= 4
                sprite_sheet.set_clip(sheet_start_x + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
                frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
                frame.set_colorkey(GRAY)
                frame2x = pygame.transform.scale2x(frame)
                self.walking_frames_l.append(frame2x)
        for i in range(6, 9):
            sprite_sheet.set_clip(sheet_start_x + 2+ (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
            frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            frame.set_colorkey(GRAY)
            frame2x = pygame.transform.scale2x(frame)
            self.walking_frames_r.append(frame2x)
            # vi kan ikke gå 0,1,2,0,1,2 vi må gå 0,1,2,1,0,1,2
            if i == 8:
                i= 7
                sprite_sheet.set_clip(sheet_start_x + 2 + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
                frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
                frame.set_colorkey(GRAY)
                frame2x = pygame.transform.scale2x(frame)
                self.walking_frames_r.append(frame2x)
        for i in range(9, 12):
            sprite_sheet.set_clip(sheet_start_x + 5 + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
            frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            frame.set_colorkey(GRAY)
            frame2x = pygame.transform.scale2x(frame)
            self.walking_frames_u.append(frame2x)
            # vi kan ikke gå 0,1,2,0,1,2 vi må gå 0,1,2,1,0,1,2
            if i == 11:
                i= 10
                sprite_sheet.set_clip(sheet_start_x + 5 + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
                frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
                frame.set_colorkey(GRAY)
                frame2x = pygame.transform.scale2x(frame)
                self.walking_frames_u.append(frame2x)



        #Set starting frame
        self.image = self.walking_frames_d[1]


        #Reference to frame rectangle
        self.rect = self.image.get_rect()
        self.rect.y = 32 # Startposition y
        self.rect.x = 32 # startposition x
        print(self.rect)

    def update(self):
        pos = hitbox.rect.y + hitbox.rect.x
        if self.direction == "D":
            frame = (pos//30 ) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]
        elif self.direction == "L":
            frame = (pos//30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "R":
            frame = (pos//30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "U":
            frame = (pos//30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]


        '''
        hitbox = pygame.sprite.Sprite
        pygame.Rect(player.rect.x + 8,player.rect.y + 34, 18 ,14 )
        '''


#####################################################################################
##############################^^^^PLAYER^^^^#########################################



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
# Grid value 1 = hardblock, 2 = softblock, 3 = empty
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

# Rammen. De brikkene som ikke kan ødelegges

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


Hitbox.walls = hardblock_list

# soft sprite blocks loads after hardblocks fordi drid må fylles opp med hardblocks
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
                grid[row][column] = 2
        elif 2 < column < 14 and BLOCKS-column > 3:
            if grid[row][column] == 0:
                softblock.rect.x = column * BLOCK_HEIGHT
                softblock.rect.y = row * BLOCK_WIDTH
                all_sprites_list.add(softblock)
                softblock_list.add(softblock)
                grid[row][column] = 2
        elif grid[row][column] == 0:
            grid[row][column] = 3

# Spilleren
player_list = pygame.sprite.Group()
player = Player()
#player.rect.x =  BLOCK_WIDTH
#player.rect.y =  BLOCK_HEIGHT
player_list.add(player)

hitbox_list = pygame.sprite.Group()
hitbox = Hitbox()
hitbox_list.add(hitbox)



'''
softblock.rect.x = column * BLOCK_HEIGHT
softblock.rect.y = row * BLOCK_WIDTH
all_sprites_list.add(softblock)
softblock_list.add(softblock)
'''

'''
# Load and set up graphics.
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)
'''

done = False

while not done:
    player_list.update()
    hitbox_list.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            column = mouse_position[0] // BLOCK_WIDTH
            row = mouse_position[1] // BLOCK_HEIGHT
            print(row, column)
            print("Grid value = ", grid[row][column])
            '''
            print(player.mask.count())
            print(player.mask.get_bounding_rects())
            '''

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                hitbox.go_down()
            if event.key == pygame.K_LEFT:
                hitbox.go_left()
            if event.key == pygame.K_RIGHT:
                hitbox.go_right()
            if event.key == pygame.K_UP:
                hitbox.go_up()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                if event.key == pygame.K_DOWN and hitbox.movement_y > 0:
                    hitbox.stop_y()
                    if hitbox.movement_x < 0:
                        hitbox.direction = "L"
                    elif hitbox.movement_x > 0:
                        hitbox.direction = "R"
            if event.key == pygame.K_LEFT:
                if event.key == pygame.K_LEFT and hitbox.movement_x < 0:
                    hitbox.stop_x()
                    if hitbox.movement_y < 0:
                        hitbox.direction = "U"
                    elif hitbox.movement_y > 0:
                        hitbox.direction = "D"
            if event.key == pygame.K_RIGHT:
                if event.key == pygame.K_RIGHT and hitbox.movement_x > 0:
                    hitbox.stop_x()
                    if hitbox.movement_y < 0:
                        hitbox.direction = "U"
                    elif hitbox.movement_y > 0:
                        hitbox.direction = "D"
            if event.key == pygame.K_UP:
                if event.key == pygame.K_UP and hitbox.movement_y < 0:
                    hitbox.stop_y()
                    if hitbox.movement_x < 0:
                        hitbox.direction = "L"
                    elif hitbox.movement_x > 0:
                        hitbox.direction = "R"
    '''
    player.mask = pygame.mask.from_surface(player.image)
    player.mask.clear()
    for width in range (34):
        for height in range(48):
            if height > 34 and 6 < width < 26:
                player.mask.set_at((width, height),1)
    '''
    # hitbox = pygame.Rect(player.rect.x + 8,player.rect.y + 34, 18 ,14)

    # blocks_hit_list = pygame.sprite.spritecollide(hitbox, hardblock_list, True)



    mouse_position = pygame.mouse.get_pos()


    '''
    mouse_position = pygame.mouse.get_pos()
    unmovable_object.rect.x = mouse_position[0]
    unmovable_object.rect.y = mouse_position[1]
    '''
    ################Her laster vi inn grafikken som ikke er sprites:#####################
    ####Denne kan gå utenom loopen?##############

    for column in range(BLOCKS):
        column_area = 0 < column < BLOCKS-1
        for row in range(BLOCKS):
            row_area = 0 < row < BLOCKS-1
            if column == 1 and row_area:
                screen.blit(field_shadow2x, [row * BLOCK_WIDTH, column * BLOCK_HEIGHT])
            else:
                screen.blit(field2x, [row * BLOCK_WIDTH, column * BLOCK_HEIGHT])

        for row in range(2, BLOCKS-1, 2):
            if (column % 2) and column_area:
                screen.blit(field_shadow2x, [row * BLOCK_WIDTH, column * BLOCK_HEIGHT])
    ####################################################################################
    # Spritene tegnes etter grafikken som ikke kan røres:
    all_sprites_list.draw(screen)
    player_list.draw(screen)
    hitbox_list.draw(screen)

    # flip skriver til screen
    pygame.display.flip()
    # klokken øker med ett
    clock.tick(60)


pygame.quit ()