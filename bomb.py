__author__ = 'Kim'

import pygame
from constants import *
from blocks import *
from player import *

class Bomb(pygame.sprite.Sprite):

    bomb_frames = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        i = 0
        sheet_start_x = 16
        sheet_start_y = 255
        frame_width = 17
        frame_height = 17
        sheet_margin = 0
        sprite_sheet = pygame.image.load("sprite_sheet0.png")
        for i in range(0, 3):
            sprite_sheet.set_clip(sheet_start_x + (frame_width+0) * i, sheet_start_y, frame_width, frame_height)
            b_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            b_frame.set_colorkey(GRAY)
            b_frame2x = pygame.transform.scale2x(b_frame)
            b_frame2x.set_colorkey(GRAY)
            self.bomb_frames.append(b_frame2x)

        self.image = self.bomb_frames[2]
        #self.image = pygame.Surface([32, 32])
        #self.image.fill(WHITE)
        #Reference to frame rectangle
        self.rect = pygame.Rect(32, 32, 32, 32)
        self.rect.y = 32  # Startposition y
        self.rect.x = 32  # startposition x
        print(self.rect)




