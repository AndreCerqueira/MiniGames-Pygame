import pygame

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

        self.image = pygame.Surface((16, 16))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)

        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 3

    def update(self, players):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        for player in players:
            if pygame.Rect.colliderect(self.rect, player) == True:
                self.speed *= -1
            


    def draw(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        #pygame.draw.circle(WIN, 'white', (self.rect.x , self.rect.y), 10)
        

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