import pygame
from settings import TILE_WIDTH, TILE_HEIGHT


# Tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, durability):
        super().__init__()

        self.image = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.rect = self.image.get_rect(topleft = pos)
        self._durability = durability
        color = self.get_durability_color(self._durability)
        self.image.fill(color)


    # Get Durability Value Function
    @property
    def durability(self):
        return self._durability


    # Set Durability Value
    @durability.setter
    def durability(self, value):
        if value <= 0:
            self.kill()
        self._durability = value
        color = self.get_durability_color(self._durability)
        self.image.fill(color)


    # Return the durability color value
    def get_durability_color(self, durability):
        switcher = {
            0: "white",
            1: "white",
            2: "green",
            3: "yellow",
            4: "orange",
            5: "red"
        }
        return switcher.get(durability)

