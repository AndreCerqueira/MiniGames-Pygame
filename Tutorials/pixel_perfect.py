import pygame
import math

pygame.init()

FPS = 60
W, H = 900, 500
HW, HH = W/2, H/2
WIN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mini tutorial!")
clock = pygame.time.Clock()

def main():

    obstacle = pygame.image.load("map.png").convert_alpha()
    obstacle_mask = pygame.mask.from_surface(obstacle)
    obstacle_rect = obstacle.get_rect()
    ox = HW - obstacle_rect.center[0]
    oy = HH - obstacle_rect.center[1]

    grenn_blob = pygame.image.load("player.png").convert_alpha()
    orange_blob = pygame.image.load("player2.png").convert_alpha()
    blob_mask = pygame.mask.from_surface(grenn_blob)
    blob_rect = grenn_blob.get_rect()
    blob_color = grenn_blob

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WIN.fill('black')

        mx, my = pygame.mouse.get_pos()

        offset = (mx - ox, my -oy)
        result = obstacle_mask.overlap(blob_mask, offset)
        if result:
            blob_color = orange_blob
        else:
            blob_color = grenn_blob

        WIN.blit(obstacle, (ox, oy))
        WIN.blit(blob_color, (mx, my))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()