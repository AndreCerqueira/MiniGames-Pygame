import pygame
from os import walk
from settings import HEIGHT, WIDTH

class Canvas():
    def __init__(self, win):

        self.win = win
        
        self.lives_image = list()
        self._lives = 3

        position = pygame.math.Vector2(20, HEIGHT-60)
        for image in range(3):
            image = pygame.transform.scale(pygame.image.load('assets/heart_full.png'), (48, 48)).convert_alpha()
            item = pygame.sprite.Sprite()
            item.image = image
            
            item.rect = image.get_rect(topleft = position)
            position.x += 60
            self.lives_image.append(item)

        font = pygame.font.SysFont('comicsans', 20)
        self.level_text = font.render("Level 1", True, 'white')
        

    # Get Lives Value Function
    @property
    def lives(self):
        return self._lives


    # Set Lives Value
    @lives.setter
    def lives(self, value):
        self._lives = value

        # Remove the last element
        if len(self.lives_image) > 0:
            self.lives_image.remove(self.lives_image[len(self.lives_image)-1])
        else:
            self.game_over()

    def draw(self):
        
        # Lives
        for live in self.lives_image:
            self.win.blit(live.image, live.rect)

        # Level Text
        self.win.blit(self.level_text, (WIDTH-(self.level_text.get_width()+20), HEIGHT-(self.level_text.get_height()+20)))


    def game_over(self):
        pass
