__author__ = 'Linux Gang'

import pygame
from constants import *
from blocks import *

class Hitbox(pygame.sprite.Sprite):

    bomb_power = 2
    bombs_placed = 0
    max_bombs = 1
    direction = "D"
    movement_x = 0
    movement_y = 0
    walls = None
    bombs = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.rect = pygame.Rect(player.rect.x + 8,player.rect.y + 34, 18 ,14)

        self.image = pygame.Surface([22, 14])
        self.image.fill(WHITE)
        self.rect = pygame.Rect(BLOCK_WIDTH + 6, BLOCK_HEIGHT + 34, 22, 14)
        for i in range(self.bomb_power):
            print(i)

    def update(self):
        self.rect.x += self.movement_x
        #self.rect.y += self.movement_y Denne kan ikke stå her oppe!
        #print(self.rect.bottom)

        # Vi kolliderer med bomben etter å ha forlatt den
        bomb_hit_list = pygame.sprite.spritecollide(self, self.bombs, False)
        for bomb in bomb_hit_list:
            if self.rect.right - self.movement_x <= bomb.rect.left: # ta med self.movement_x > 0 hvis det bugger
                self.rect.right = bomb.rect.left
            elif self.rect.left - self.movement_x >= bomb.rect.right:
                self.rect.left = bomb.rect.right
            elif self.rect.bottom - self.movement_y <= bomb.rect.top:
                self.rect.bottom = bomb.rect.top
            elif self.rect.top - self.movement_y >= bomb.rect.bottom:
                self.rect.top = bomb.rect.bottom

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.movement_x > 0:
                self.rect.right = block.rect.left
                if self.movement_y == 0 and block.rect.x < SCREEN_HEIGHT - BLOCK_WIDTH and type(block == type(hardblock)):
                    if self.rect.centery - 12 > block.rect.centery:
                        self.rect.y += 1
                    elif self.rect.centery + 12 < block.rect.centery:
                        self.rect.y -= 1
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                if self.movement_y == 0 and block.rect.x > 0 and type(block == type(hardblock)):
                    if self.rect.centery - 12 > block.rect.centery:
                        self.rect.y += 1
                    elif self.rect.centery + 12 < block.rect.centery:
                        self.rect.y -= 1
        # Move up/down
        self.rect.y += self.movement_y  # jævlig spesiellt at denne linjen måtte stå akkurat her

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.movement_y > 0:
                self.rect.bottom = block.rect.top
                if type(block == type(hardblock)) and self.movement_x == 0 and block.rect.y < SCREEN_HEIGHT - BLOCK_HEIGHT:
                    if self.rect.centerx - 12 > block.rect.centerx:
                        self.rect.x += 1
                    elif self.rect.centerx + 12 < block.rect.centerx:
                        self.rect.x -= 1
            else:
                self.rect.top = block.rect.bottom
                if type(block == type(hardblock)) and self.movement_x == 0 and block.rect.y > 0:
                    if self.rect.centerx - 12 > block.rect.centerx:
                        self.rect.x += 1
                    elif self.rect.centerx + 12 < block.rect.centerx:
                        self.rect.x -= 1



    def go_down(self):
        self.movement_y = 2
        self.direction = "D"

    def go_left(self):
        self.movement_x = -2
        self.direction = "L"

    def go_right(self):
        self.movement_x = 2
        self.direction = "R"

    def go_up(self):
        self.movement_y = -2
        self.direction = "U"

    def stop_x(self):
        self.movement_x = 0
        self.rect.x += self.movement_x

    def stop_y(self):
        self.movement_y = 0
        self.rect.y += self.movement_y

    def bomb_gone(self):
        self.bombs_placed -= 1

    def die(self):
        self.kill()



class Player(pygame.sprite.Sprite):

    frame_count = 0
    FRAME_RATE = 60
    seconds = frame_count // FRAME_RATE
    # vi setter startverdiene til Player:
    movement_x = 0
    movement_y = 0

    # Liste med de forskjellige bevegelses bildene, listen er tom nå:
    walking_frames_d = []
    walking_frames_u = []
    walking_frames_l = []
    walking_frames_r = []
    dying_frames = []

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
                i = 1
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
                i = 4
                sprite_sheet.set_clip(sheet_start_x + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
                frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
                frame.set_colorkey(GRAY)
                frame2x = pygame.transform.scale2x(frame)
                self.walking_frames_l.append(frame2x)
        for i in range(6, 9):
            sprite_sheet.set_clip(sheet_start_x + 2 + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
            frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            frame.set_colorkey(GRAY)
            frame2x = pygame.transform.scale2x(frame)
            self.walking_frames_r.append(frame2x)
            # vi kan ikke gå 0,1,2,0,1,2 vi må gå 0,1,2,1,0,1,2
            if i == 8:
                i = 7
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
                i = 10
                sprite_sheet.set_clip(sheet_start_x + 5 + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
                frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
                frame.set_colorkey(GRAY)
                frame2x = pygame.transform.scale2x(frame)
                self.walking_frames_u.append(frame2x)
        for i in range(16, 20):
            v = 4
            if i == 17:
                v = 3
            elif i == 18:
                v = 2
            elif i == 19:
                v = 0
            sprite_sheet.set_clip(sheet_start_x + v + (frame_width+sheet_margin) * i, sheet_start_y, frame_width, frame_height)
            frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            frame.set_colorkey(GRAY)
            frame2x = pygame.transform.scale2x(frame)
            self.dying_frames.append(frame2x)

        #Set starting frame
        self.image = self.walking_frames_d[1]
        #Reference to frame rectangle
        self.rect = self.image.get_rect()
        self.rect.y = 32  # Startposition y
        self.rect.x = 32  # startposition x

    def update(self):

        self.rect.x = hitbox.rect.x - 6
        self.rect.y = hitbox.rect.y - 34

        pos = hitbox.rect.y + hitbox.rect.x
        if hitbox.direction == "D":
            frame = (pos//30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]
        elif hitbox.direction == "L":
            frame = (pos//30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif hitbox.direction == "R":
            frame = (pos//30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif hitbox.direction == "U":
            frame = (pos//30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]




# Spilleren

player = Player()
hitbox = Hitbox()
