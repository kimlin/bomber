__author__ = 'Kim'

import pygame
from player import *
from constants import *
from blocks import *

'''
hitbox størrelse
animasjon? pos // 30
'''

# Call this function so the Pygame library can initialize itself
pygame.init()
# Create screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# caption name:
pygame.display.set_caption(CAPTION_NAME)
# Create a clock:
clock = pygame.time.Clock()

#sprite_lists
all_sprites_list = pygame.sprite.Group()
hardblock_list = pygame.sprite.Group()
softblock_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
hitbox_list = pygame.sprite.Group()
bomb_list = pygame.sprite.Group()
player_list.add(player)
hitbox_list.add(hitbox)
#bomb_list.add(bomb)
Hitbox.walls = wall_list

# Hardblocks
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
            wall_list.add(hardblock)
            grid[row][column] = 1
        elif row == 0 and column_area or row == BLOCKS-1 and column_area:
            hardblock.rect.x = column * BLOCK_HEIGHT
            hardblock.rect.y = row * BLOCK_WIDTH
            all_sprites_list.add(hardblock)
            hardblock_list.add(hardblock)
            wall_list.add(hardblock)
            grid[row][column] = 1
    for row in range(2, BLOCKS-1, 2):
        hardblock = HardBlock()
        column_area = 0 < column < BLOCKS-1
        if not (column % 2) and column_area:
            hardblock.rect.x = column * BLOCK_HEIGHT
            hardblock.rect.y = row * BLOCK_WIDTH
            all_sprites_list.add(hardblock)
            hardblock_list.add(hardblock)
            wall_list.add(hardblock)
            grid[row][column] = 1

# Softblocks
for column in range(BLOCKS):
    for row in range(BLOCKS):
        softblock = SoftBlock()
        if 2 < row < 14 and BLOCKS-row > 3:
            if grid[row][column] == 0:
                softblock.rect.x = column * BLOCK_HEIGHT
                softblock.rect.y = row * BLOCK_WIDTH
                all_sprites_list.add(softblock)
                softblock_list.add(softblock)
                wall_list.add(softblock)
                grid[row][column] = 2
        elif 2 < column < 14 and BLOCKS-column > 3:
            if grid[row][column] == 0:
                softblock.rect.x = column * BLOCK_HEIGHT
                softblock.rect.y = row * BLOCK_WIDTH
                all_sprites_list.add(softblock)
                softblock_list.add(softblock)
                wall_list.add(softblock)
                grid[row][column] = 2
        elif grid[row][column] == 0:
            grid[row][column] = 3


# Main Loop
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            column = mouse_position[0] // BLOCK_WIDTH
            row = mouse_position[1] // BLOCK_HEIGHT
            print(row, column)
            #print(player_column, player_row)
            print("Grid value = ", grid[row][column])







        # Tastetrykk ned:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                hitbox.go_down()
            if event.key == pygame.K_LEFT:
                hitbox.go_left()
            if event.key == pygame.K_RIGHT:
                hitbox.go_right()
            if event.key == pygame.K_UP:
                hitbox.go_up()
            if event.key == pygame.K_SPACE:
                player_column = hitbox.rect.centerx // BLOCK_WIDTH
                player_row = hitbox.rect.centery // BLOCK_HEIGHT
                bomb = Bomb()
                bomb.rect.x = player_column * BLOCK_HEIGHT
                bomb.rect.y = player_row * BLOCK_WIDTH
                bomb_list.add(bomb)



        # Tastetrykk slippes:
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

    mouse_position = pygame.mouse.get_pos()
    player_list.update()
    hitbox_list.update()
    if len(bomb_list) > 0:
        bomb_list.update()
    '''
    seconds = FRAME_COUNT // FRAME_RATE
    FRAME_COUNT += 1
    '''



    # Grafikk:
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
    # Sprites:
    all_sprites_list.draw(screen)
    bomb_list.draw(screen)
    player_list.draw(screen)
    #hitbox_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit ()