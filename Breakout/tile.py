import pygame
from settings import TILE_WIDTH, TILE_HEIGHT


# Tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, durability):
        super().__init__()

        self.image = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.rect = self.image.get_rect(topleft = pos)
        self._durability = durability
        #color = self.get_durability_color(self._durability)
        self.image.fill('red')

    # Get Function
    @property
    def durability(self):
        return self._durability

    # Set Function
    @durability.setter
    def durability(self, value):
        self._durability -= value
        print(self._durability)
        color = self.get_durability_color(self._durability)
        self.image.fill(color)

    def get_durability_color(self, durability):

        switcher = {
            1: "white",
            2: "green",
            3: "yellow",
            4: "orange",
            5: "red"
        }

        return switcher.get(durability)

    def update():
        pass