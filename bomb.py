__author__ = 'Kim'

import pygame
from constants import *
from blocks import *

#Importerer alle funksjoner fra "player"
from player import *

# NB:Det er viktig at import ikke importerer hverandre, husker du hvorfor kim?


#klassen "bomb" blir definert her
class Bomb(pygame.sprite.Sprite):

    bomb_frames = []
    tick = 0
    frame_count = 0
    FRAME_RATE = 60
    seconds = frame_count // FRAME_RATE
    seconds_b = seconds
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
        grid[player_row][player_column] = 3
        hitbox.bomb_gone()



