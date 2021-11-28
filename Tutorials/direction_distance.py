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

    x, y = HW, HH
    pmx, pmy = x, y # previous location
    dx, dy = 0, 0 # direction to travel
    distance = 0
    speed = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        m = pygame.mouse.get_pressed()
        if m[0] and not distance:
            mx, my = pygame.mouse.get_pos()

            radians = math.atan2(my - pmy, mx - pmx)
            distance = math.hypot(mx - pmx, my - pmy) / speed
            distance = int(distance)

            dx = math.cos(radians) * speed
            dy = math.sin(radians) * speed

            pmx, pmy = mx, my

        if distance:
            distance -= 1
            x += dx
            y += dy

        WIN.fill('black')

        pygame.draw.circle(WIN, 'white', (int(x), int(y)), 25, 0)
        if distance:
            pygame.draw.circle(WIN, 'red', (pmx, pmy), 5, 0)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()