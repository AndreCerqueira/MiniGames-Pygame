import pygame
from settings import *


# Tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

    def update():
        pass