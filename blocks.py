__author__ = 'Kim'


#importerer pygame
import pygame
#importerer alle funksjoner fra "player"
from player import *
#importerer alle funksjoner fra "constans"
from constants import *


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

hardblock = HardBlock()