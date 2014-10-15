__author__ = 'Kim'


#importerer pygame/ import pygame
import pygame

#importerer alle funksjoner fra "player" / imporst all the functions of "player"
from player import *

#importerer alle funksjoner fra "constans" / imports all the functions of "Constans"
from constants import *

#klasse "Hardblock"
class HardBlock(pygame.sprite.Sprite):

    def __init__(self):

    # Kaller på foreldre klassen (Sprite) konstruktoren /Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Laster bildet /Load the image
        self.image = hard_block2x

        # Setter vår gjennomsiktige farge /Set our transparent color
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()


class SoftBlock(pygame.sprite.Sprite):

    def __init__(self):

    # Kaller på foreldre klassen (Sprite) konstruktoren /Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Laster bildet /Load the image
        self.image = soft_block2x

        # Setter vår gjennomsiktige farge / Set our transparent color
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

hardblock = HardBlock()