import pygame
import random
from sys import exit


pygame.init()
screen = pygame.display.set_mode((600, 900))


# Images
background = pygame.image.load("Game/graphics/background.jpg").convert_alpha()
palyer = pygame.image.load("Game/graphics/background.jpg").convert_alpha()
screen_w, screen_h = screen.get_size()
image_w, image_h = background.get_size()


# Pygame configs
clock = pygame.time.Clock()
pygame.display.set_caption("Doodle jump")

while True:
    # if close window is pressed the game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for x in range(0, screen_w, image_w):
        for y in range(0, screen_h, image_h):
            screen.blit(background, (x, y))

    pygame.display.update()
    clock.tick(60)
