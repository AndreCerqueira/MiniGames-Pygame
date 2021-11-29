import pygame
from settings import *


# Player
class Player(pygame.sprite.Sprite):
    def __init__(self, win, pos, size):
        super().__init__()

        self.win = win
        self.image = pygame.Surface(size)
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_a] and self.rect.x > 0):
            self.rect.x -= self.speed
        if (keys[pygame.K_d] and self.rect.x < WIDTH - self.image.get_width()):
            self.rect.x += self.speed
