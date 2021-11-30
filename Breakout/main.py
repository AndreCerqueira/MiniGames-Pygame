import pygame, sys

from settings import *
from player import Player
from ball import Ball
from level import Level


# Pygame setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# Events
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():

    # Game Setup
    player = Player(WIN, (WIDTH/2-50, HEIGHT-100), (100, 10))
    ball = Ball(WIN, (WIDTH/2-16, HEIGHT/2-16), (16, 16))

    level = Level(LEVEL_MAP, WIN)

    # Game Loop
    while True:
        events()

        player.update()
        ball.update()

        # Collision with player
        if pygame.sprite.collide_mask(ball, player):
            ball.bounce()

        # Detect colision with tiles
        for tile in level.tiles:
            collision = tile.rect.colliderect(ball.rect)
            if collision:
                tile.durability -= 1
                #ball.bounce()
                #if tile.durability <= 0:
                level.tiles.remove(tile)

        # Draw tiles
        for tile in level.tiles:
            WIN.blit(tile.image, tile.rect)

        WIN.blit(player.image, player.rect)
        pygame.draw.circle(WIN, 'white', (ball.rect.x, ball.rect.y), 10)

        pygame.display.update()
        clock.tick(60)
        WIN.fill('black')


if __name__ == "__main__":
    main()