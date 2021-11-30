import pygame
import random
from settings import WIDTH, HEIGHT


# Ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, win, pos, size):
        super().__init__()

        self.win = win
        self.image = pygame.Surface(size)
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

        self.velocity = pygame.math.Vector2(0, 3) # random.randint(4, 8) random.randint(-8, 8)


    def update(self):
        # Movement
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Collision with borders
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.velocity.x *= -1
        if self.rect.y < 0:
            self.velocity.y *= -1


    def bounce(self):
        self.velocity.x = random.randint(-8, 8)
        self.velocity.y *= -1


    def respawn(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velocity = pygame.math.Vector2(0, 3)