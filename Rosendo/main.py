from turtle import position
import pygame
from sys import exit
import random

class snailO:
    def __init__(self,):
        self.position=810
    
    def move(self,):
        screen.blit(snail,[self.position,265])
        if self.position>=-100:
            self.position-=3
        else:
            del self


pygame.init()
screen = pygame.display.set_mode((800, 400))

#Imagenes
background_image = pygame.image.load("Rosendo\graphics\Sky.png")
floor = pygame.image.load("Rosendo/graphics/ground.png")
snail = pygame.image.load('Rosendo/graphics/snail/snail1.png')

#Configuraciones del juego
pygame.display.set_caption("Rosendo, Be Careful!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Rosendo/font/Pixeltype.ttf", 50)
pygame.display.set_icon(snail)
text_surface = test_font.render("START!", False, "Black")

snails=[]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    screen.blit(background_image, [0, 0])
    screen.blit(floor, [0, 300])
    screen.blit(text_surface,[350,50])

    if random.random()>.99:
        snails.append(snailO())

    for i in snails:
        i.move()

    clock.tick(60)


