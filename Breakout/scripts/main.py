import pygame, sys
from canvas import Canvas

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


# Collisions
def collisions(ball, player, canvas, tiles):
    # Detect collision with player
    if pygame.sprite.collide_mask(ball, player):
        ball.bounce()

    # Detect colision with tiles
    tile_collision_list = pygame.sprite.spritecollide(ball, tiles, False)
    for tile in tile_collision_list:
        ball.bounce()
        tile.durability -= 1

    # Detect lost ball
    if ball.rect.y > HEIGHT:
        ball.respawn((WIDTH/2-16, HEIGHT/2-16))
        canvas.lives -= 1


# Drawings
def draw(ball, player, canvas, level):
    # Draw tiles
    for tile in level.tiles:
        WIN.blit(tile.image, tile.rect)

    # Draw player and ball
    WIN.blit(player.image, player.rect)
    pygame.draw.circle(WIN, 'white', (ball.rect.x, ball.rect.y), 10)

    # Draw Canvas
    canvas.draw(str(level.current_level))


def main():

    # Game Setup
    player = Player(WIN, (WIDTH/2-50, HEIGHT-100), (100, 10))
    ball = Ball(WIN, (WIDTH/2-16, HEIGHT/2-16), (16, 16))
    canvas = Canvas(WIN)
    level = Level(levels[1], WIN)

    # Game Loop
    while True:
        events()

        # Update Movements
        player.update()
        ball.update()
        level.update()

        # Check Collisions
        collisions(ball, player, canvas, level.tiles)

        # Draw Everything
        draw(ball, player, canvas, level)

        pygame.display.update()
        clock.tick(60)
        WIN.fill('black')


if __name__ == "__main__":
    main()