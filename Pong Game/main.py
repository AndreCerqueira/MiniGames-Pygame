import pygame
import math
import random

pygame.init()

FPS = 60
VEL = 5
WIDTH, HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, up, down, color):
        super().__init__()

        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)

        self.up = up
        self.down = down


    def movement(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up] and self.rect.y - VEL > 0: # Up
            self.rect.y -= VEL
        if keys_pressed[self.down] and self.rect.y + VEL + PLAYER_HEIGHT < HEIGHT - 15: # Down
            self.rect.y += VEL


    def update(self):
        self.movement()


    def draw(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Render Properties
        self.image = pygame.Surface((16, 16))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)

        # Psysics Properties
        self.previous_location = pygame.math.Vector2(WIDTH, HEIGHT/2)
        self.direction = pygame.math.Vector2(0, 0)    
        self.distance = 0
        self.speed = 3
        self.side = 'left'

        # Throw the ball
        self.change_direction()


    def update(self, players):

        if pygame.Rect.colliderect(self.rect, players[0]) == True and self.side == 'left':
            self.side = 'right'
            self.change_direction()
        elif pygame.Rect.colliderect(self.rect, players[1]) == True and self.side == 'right':
            self.side = 'left'
            self.change_direction()
        
        if self.distance:
            self.distance -= 1
            self.rect.x += self.direction.x
            self.rect.y += self.direction.y
   

    def draw(self):
        pygame.draw.circle(WIN, 'white', (self.rect.x , self.rect.y), 10)
    

    def change_direction(self):

        destination = pygame.math.Vector2(0, random.randint(0, HEIGHT))

        if self.side == 'left':
            destination.x = 0
        else:
            destination.x = WIDTH

        pmx, pmy = self.previous_location

        radians = math.atan2(destination.x - pmy, destination.y - pmx)
        distance = math.hypot(destination.x - pmx, destination.y - pmy) / self.speed
        self.distance = int(distance)

        self.direction.x = math.cos(radians) * self.speed
        self.direction.y = math.sin(radians) * self.speed

        self.previous_location = destination

def main():

    # Game Setup
    player_red = Player((100, (HEIGHT/2)-(PLAYER_HEIGHT/2)), pygame.K_w, pygame.K_s, 'red')
    player_blue = Player((WIDTH-100, (HEIGHT/2)-(PLAYER_HEIGHT/2)), pygame.K_UP, pygame.K_DOWN, 'blue')
    ball = Ball((WIDTH/2,HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WIN.fill('black')

        player_red.update()
        player_blue.update()

        ball.update((player_red, player_blue))
        ball.draw()

        player_red.draw()
        player_blue.draw()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()