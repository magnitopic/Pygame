import pygame
import random
from sys import exit


pygame.init()
screen = pygame.display.set_mode((350, 600))

# Images
background = pygame.image.load("doodleJump/graphics/background.jpg").convert_alpha()
player = pygame.image.load("doodleJump/graphics/normal.png").convert_alpha()
leafImage = pygame.image.load("doodleJump/graphics/leaf.png").convert_alpha()
screen_w, screen_h = screen.get_size()
image_w, image_h = background.get_size()


# Pygame configs
clock = pygame.time.Clock()
pygame.display.set_caption("Doodle jump")
pygame.display.set_icon(player)


class leaf:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 350)
    def draw():
        snail_rectangle = leafImage.get_rect(midbottom =(x,y))
        screen.blit(leafImage,snail_rectangle)

while True:
    # if close window button is pressed the game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    leaf()
    #Draw repeating background
    for x in range(0, screen_w, image_w):
        for y in range(0, screen_h, image_h):
            screen.blit(background, (x, y))

    pygame.display.update()
    clock.tick(60)
