import pygame
from settings import TILE_HEIGHT, TILE_OFFSET, TILE_WIDTH, levels
from tile import Tile

class Level():
    def __init__(self, level_data, win):
        
        self.current_level = 1
        self.tiles = pygame.sprite.Group()
        self.setup_map(level_data)
        self.win = win

    def setup_map(self, level_data):

        x, y = 0, 0
        offset = pygame.math.Vector2(0, 0)
        for row_index, row in enumerate(level_data):
            offset.y += TILE_OFFSET * 2
            offset.x = 0
            for cell_index, cell in enumerate(row):
                offset.x += TILE_OFFSET * 2
                if cell != " ":
                    x = cell_index * TILE_WIDTH + offset.x
                    y = row_index * TILE_HEIGHT + offset.y
                    tile = Tile((x, y), int(cell))
                    self.tiles.add(tile)

    def update(self):

        if len(self.tiles) <= 0:
            self.current_level += 1
            self.setup_map(levels[self.current_level])
            
