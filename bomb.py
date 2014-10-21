__author__ = 'Linux Gang'

import pygame
from constants import *
from blocks import *
from player import *
from explosions import *

# NB:Det er viktig at import ikke importerer hverandre,
# da vil de importere hverandre i en evig loop og aldri komme ned i koden


#klassen "bomb" blir definert her
class Bomb(pygame.sprite.Sprite):

    l = 1
    r = 1
    d = 1
    u = 1
    bomb_frames = []
    tick = 0
    frame_count = 0
    FRAME_RATE = 60
    seconds = frame_count // FRAME_RATE
    players = None


    def __init__(self):

        # Kaller på foreldre klassen (Sprite) konstruktoren /Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)


        i = 0
        sheet_start_x = 16
        sheet_start_y = 256
        frame_width = 17
        frame_height = 16
        sprite_sheet = pygame.image.load("sprite_sheet0.png")
        for i in range(0, 3):
            sprite_sheet.set_clip(sheet_start_x + (frame_width+0) * i, sheet_start_y, frame_width, frame_height)
            b_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            b_frame.set_colorkey(GRAY)
            b_frame2x = pygame.transform.scale2x(b_frame)
            b_frame2x.set_colorkey(GRAY)
            self.bomb_frames.append(b_frame2x)

        self.image = self.bomb_frames[0]
        #Reference to frame rectangle
        self.rect = pygame.Rect(32, 32, 32, 32)
        self.rect.y = 32  # Startposition y
        self.rect.x = 32  # startposition x

    def update(self):

        self.seconds = self.frame_count*2 // self.FRAME_RATE
        self.frame_count += 1
        if self.seconds == 3:
            self.seconds = 0
            self.frame_count = 0
            self.tick += 1
            if self.tick == 2:
                self.explode()
        self.image = self.bomb_frames[self.seconds]



    def explode(self):
        player_column = self.rect.centerx // BLOCK_WIDTH
        player_row = self.rect.centery // BLOCK_HEIGHT
        self.kill()
        grid[player_row][player_column] = 3  # Denne linjen gjør at vi kan legge bomber her igjen
        ex = Explosions(4)
        ex.rect.x = self.rect.x
        ex.rect.y = self.rect.y
        explosion_list.add(ex)
        while self.l <= hitbox.bomb_power and grid[player_row][player_column + self.l] != 1:
            if self.l == hitbox.bomb_power:
                ex = Explosions(6)
                ex.rect.x = self.rect.x + (self.l * BLOCK_WIDTH)
                ex.rect.y = self.rect.y
                explosion_list.add(ex)
                self.l += 1
            else:
                ex = Explosions(5)
                ex.rect.x = self.rect.x + (self.l * BLOCK_WIDTH)
                ex.rect.y = self.rect.y
                explosion_list.add(ex)
                self.l += 1
        while self.r <= hitbox.bomb_power and grid[player_row][player_column - self.r] != 1:
            if self.r == hitbox.bomb_power:
                ex = Explosions(2)
                ex.rect.x = self.rect.x - (self.r * BLOCK_WIDTH)
                ex.rect.y = self.rect.y
                explosion_list.add(ex)
                self.r += 1
            else:
                ex = Explosions(3)
                ex.rect.x = self.rect.x - (self.r * BLOCK_WIDTH)
                ex.rect.y = self.rect.y
                explosion_list.add(ex)
                self.r += 1
        while self.d <= hitbox.bomb_power and grid[player_row + self.d][player_column] != 1:
            if self.d == hitbox.bomb_power:
                ex = Explosions(8)
                ex.rect.x = self.rect.x
                ex.rect.y = self.rect.y + (self.d * BLOCK_HEIGHT)
                explosion_list.add(ex)
                self.d += 1
            else:
                ex = Explosions(7)
                ex.rect.x = self.rect.x
                ex.rect.y = self.rect.y + (self.d * BLOCK_HEIGHT)
                explosion_list.add(ex)
                self.d += 1
        while self.u <= hitbox.bomb_power and grid[player_row - self.u][player_column] != 1:
            if self.u == hitbox.bomb_power:
                ex = Explosions(0)
                ex.rect.x = self.rect.x
                ex.rect.y = self.rect.y - (self.u * BLOCK_HEIGHT)
                explosion_list.add(ex)
                self.u += 1
            else:
                ex = Explosions(1)
                ex.rect.x = self.rect.x
                ex.rect.y = self.rect.y - (self.u * BLOCK_HEIGHT)
                explosion_list.add(ex)
                self.u += 1
        hitbox.bomb_gone()



