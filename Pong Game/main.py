import pygame, sys
import math
import random

pygame.init()

FPS = 60
VEL = 5
WIDTH, HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 10, 100
FONT = pygame.font.SysFont('comicsans', 40)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, up, down, color):
        super().__init__()

        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)

        self.score = 0
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
        self.velocity = pygame.math.Vector2(random.randint(4, 8), random.randint(-8, 8))


    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
   

    def draw(self):
        pygame.draw.circle(WIN, 'white', (self.rect.x , self.rect.y), 10)


    def bounce(self):
        self.velocity.x *= -1
        self.velocity.y = random.randint(-8, 8)
    
def draw_scores(players):

    score_red = FONT.render(str(players[0].score), True, 'white')
    score_blue = FONT.render(str(players[1].score), True, 'white')

    WIN.blit(score_red, (30, 10))
    WIN.blit(score_blue, (WIDTH-(score_blue.get_width()+30), 10))

def main():

    # Game Setup
    player_red = Player((100, (HEIGHT/2)-(PLAYER_HEIGHT/2)), pygame.K_w, pygame.K_s, 'red')
    player_blue = Player((WIDTH-100, (HEIGHT/2)-(PLAYER_HEIGHT/2)), pygame.K_UP, pygame.K_DOWN, 'blue')
    ball = Ball((WIDTH/2,HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Detect collisions with borders
        if ball.rect.x > WIDTH:
            ball.velocity.x *= -1
            player_red.score += 1

        if ball.rect.x < 0:
            ball.velocity.x *= -1
            player_blue.score += 1

        if ball.rect.y > HEIGHT or ball.rect.y < 0:
            ball.velocity.y *= -1

        # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, player_red) or pygame.sprite.collide_mask(ball, player_blue):
            ball.bounce()

        player_red.update()
        player_blue.update()
        ball.update()

        draw_scores((player_red, player_blue))
        ball.draw()
        player_red.draw()
        player_blue.draw()

        pygame.display.update()
        clock.tick(FPS)
        WIN.fill('black')


if __name__ == "__main__":
    main()