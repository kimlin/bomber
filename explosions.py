__author__ = 'Linux Gang'

import pygame
from constants import *
from blocks import *
from player import *

explosion_list = pygame.sprite.Group()
class Explosion(pygame.sprite.Sprite):

    mid_frames = []
    frame_count = 0
    FRAME_RATE = 60
    seconds = frame_count // FRAME_RATE


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        mid_start_x_frames = [185, 266, 349, 434, 518]
        sheet_start_y = 290
        frame_width = 16
        frame_height = 16
        sprite_sheet = pygame.image.load("sprite_sheet0.png")
        for i in range(0, 5):
            sprite_sheet.set_clip(mid_start_x_frames[i], sheet_start_y, frame_width, frame_height)
            e_mid_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            e_mid_frame.set_colorkey(GRAY)
            e_mid_frame2x = pygame.transform.scale2x(e_mid_frame)
            e_mid_frame2x.set_colorkey(GRAY)
            self.mid_frames.append(e_mid_frame2x)

        self.image = self.mid_frames[0]
        #Reference to frame rectangle
        self.rect = pygame.Rect(32, 32, 32, 32)
        self.rect.y = 32  # Startposition y
        self.rect.x = 32  # startposition x

    def update(self):

        self.seconds = self.frame_count*5 // self.FRAME_RATE
        self.frame_count += 1
        if self.seconds == 5:
            self.kill()
            print("dead")
            self.seconds = 0
        self.image = self.mid_frames[self.seconds]