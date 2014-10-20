__author__ = 'Linux Gang'

import pygame
from constants import *
from blocks import *
from player import *

explosion_list = pygame.sprite.Group()
class Explosions(pygame.sprite.Sprite):

    mid_frames = []
    vert_frames_t = []
    vert_frames_b = []
    hor_frames_r = []
    hor_frames_l = []
    top_frames = []
    bot_frames = []
    right_frames = []
    left_frames = []
    frame_count = 0
    FRAME_RATE = 60
    seconds = frame_count // FRAME_RATE
    i = 0


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x_frames = [185, 266, 349, 434, 518]
        sheet_start_y = 290
        frame_width = 16
        frame_height = 16
        sprite_sheet = pygame.image.load("sprite_sheet0.png")
        for i in range(0, 5):
            sprite_sheet.set_clip(x_frames[i], sheet_start_y, frame_width, frame_height)
            mid_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            mid_frame.set_colorkey(GRAY)
            mid_frame2x = pygame.transform.scale2x(mid_frame)
            mid_frame2x.set_colorkey(GRAY)
            self.mid_frames.append(mid_frame2x)

        for i in range(0, 5):
            sprite_sheet.set_clip(x_frames[i] + frame_width, sheet_start_y, frame_width, frame_height)
            hor_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            hor_frame.set_colorkey(GRAY)
            hor_frame2x = pygame.transform.scale2x(hor_frame)
            hor_frame2x.set_colorkey(GRAY)
            hor_frame_l2x = pygame.transform.flip(hor_frame2x, True, False)
            hor_frame_l2x.set_colorkey(GRAY)
            self.hor_frames_r.append(hor_frame2x)
            self.hor_frames_l.append(hor_frame_l2x)

        for i in range(0, 5):
            sprite_sheet.set_clip(x_frames[i] + (frame_width * 2), sheet_start_y, frame_width, frame_height)
            right_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            right_frame.set_colorkey(GRAY)
            right_frame2x = pygame.transform.scale2x(right_frame)
            right_frame2x.set_colorkey(GRAY)
            left_frame2x = pygame.transform.flip(right_frame2x, True, False)
            left_frame2x.set_colorkey(GRAY)
            self.right_frames.append(right_frame2x)
            self.left_frames.append(left_frame2x)

        self.vert_frames_b = self.vert_frames_t
        sheet_start_y = 274
        for i in range(0, 5):
            sprite_sheet.set_clip(x_frames[i], sheet_start_y, frame_width, frame_height)
            vert_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            vert_frame.set_colorkey(GRAY)
            vert_frame2x = pygame.transform.scale2x(vert_frame)
            vert_frame2x.set_colorkey(GRAY)
            self.vert_frames_t.append(vert_frame2x)

        self.vert_frames_b = self.vert_frames_t

        sheet_start_y = 258
        for i in range(0, 5):
            sprite_sheet.set_clip(x_frames[i], sheet_start_y, frame_width, frame_height)
            top_frame = sprite_sheet.subsurface(sprite_sheet.get_clip())
            top_frame.set_colorkey(GRAY)
            top_frame2x = pygame.transform.scale2x(top_frame)
            bot_frame2x = pygame.transform.flip(top_frame2x, False, True)
            top_frame2x.set_colorkey(GRAY)
            bot_frame2x.set_colorkey(GRAY)
            self.top_frames.append(top_frame2x)
            self.bot_frames.append(bot_frame2x)



        self.image = self.mid_frames[0]
        #Reference to frame rectangle
        self.rect = pygame.Rect(32, 32, 32, 32)
        self.rect.y = 32  # Startposition y
        self.rect.x = 32  # startposition x

    def update(self):
        #  må lage en boolean her en plass
        self.seconds = self.frame_count*5 // self.FRAME_RATE
        self.frame_count += 1
        if self.seconds == 5:
            self.kill()
            print("dead")
            self.seconds = 0
        self.image = self.left_frames[self.seconds]
        hitbox_hit_list = pygame.sprite.spritecollide(self, self.hitbox, False)
        for hitbox in hitbox_hit_list:
            bomber = hitbox
        if len(hitbox_hit_list) > 0:
            player_hit_list = pygame.sprite.spritecollide(self, self.player, False)
            for player in player_hit_list:
                self.seconds = self.frame_count*7 // self.FRAME_RATE
                self.frame_count += 1
                if self.seconds == 4:
                    player.kill()
                    bomber.die()
                    self.seconds = 0
                player.image = player.dying_frames[self.seconds]
                        #bomber.die()


