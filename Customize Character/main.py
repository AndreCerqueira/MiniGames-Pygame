import pygame, sys, os

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bgColor = (97, 165, 195)

# FONT
TEXT_FONT = pygame.font.SysFont('arial', 20)
hat_text = TEXT_FONT.render("Hat", 1, 'black')

# UI
TEXT_BACK_IMAGE = pygame.image.load(os.path.join('images/ui/text_back.png'))
TEXT_BACK_IMAGE = pygame.transform.scale(TEXT_BACK_IMAGE, (TEXT_BACK_IMAGE.get_size()[0] * 5, TEXT_BACK_IMAGE.get_size()[1] * 5))
IMAGE_BACK_IMAGE = pygame.image.load(os.path.join('images/ui/image_back.png'))
IMAGE_BACK_IMAGE = pygame.transform.scale(IMAGE_BACK_IMAGE, (IMAGE_BACK_IMAGE.get_size()[0] * 5, IMAGE_BACK_IMAGE.get_size()[1] * 5))
L_ARROW = pygame.image.load(os.path.join('images/ui/arrow_left.png'))
L_ARROW = pygame.transform.scale(L_ARROW, (L_ARROW.get_size()[0] * 5, L_ARROW.get_size()[1] * 5))
R_ARROW = pygame.image.load(os.path.join('images/ui/arrow_right.png'))
R_ARROW = pygame.transform.scale(R_ARROW, (R_ARROW.get_size()[0] * 5, R_ARROW.get_size()[1] * 5))

PLAYER_IMAGE = pygame.image.load(os.path.join('images/player2.png'))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_IMAGE.get_size()[0] * 5, PLAYER_IMAGE.get_size()[1] * 5))

# HATS
HAT1_IMAGE = pygame.image.load(os.path.join('images/hat.png'))
HAT1_IMAGE = pygame.transform.scale(HAT1_IMAGE, (HAT1_IMAGE.get_size()[0] * 5, HAT1_IMAGE.get_size()[1] * 5))
HAT2_IMAGE = pygame.image.load(os.path.join('images/hat2.png'))
HAT2_IMAGE = pygame.transform.scale(HAT2_IMAGE, (HAT2_IMAGE.get_size()[0] * 5, HAT2_IMAGE.get_size()[1] * 5))

hats = (HAT1_IMAGE, HAT2_IMAGE)

current_hat = 0

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            
            if (current_hat+1 > len(hats)-1):
                current_hat = 0
            else:
                print(current_hat)
                current_hat += 1


def next_cicle_update():
    pygame.display.update()
    clock.tick(60)
    WIN.fill(bgColor)


def main():

    current_hat = 0
    
    while True:
        events()

        # Player
        WIN.blit(PLAYER_IMAGE, (50, HEIGHT/2-PLAYER_IMAGE.get_height()/2))

        # Canvas

        # UI HAT
        WIN.blit(TEXT_BACK_IMAGE, (WIDTH-300, 50))
        WIN.blit(IMAGE_BACK_IMAGE, (WIDTH-260, 100))
        WIN.blit(hat_text, (WIDTH - 200, 60))
        WIN.blit(L_ARROW, (WIDTH-300, 150))
        WIN.blit(R_ARROW, (WIDTH-85, 150))
        WIN.blit(hats[current_hat], (WIDTH-250, 150))

        next_cicle_update()


if __name__ == "__main__":
    main()