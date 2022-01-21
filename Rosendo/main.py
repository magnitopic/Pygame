from turtle import position
import pygame
from sys import exit
import random

class snailO:
    def __init__(self,):
        self.position=810
    
    def move(self,):
        snail_rectangle = snail.get_rect(midbottom =(self.position,300))
        screen.blit(snail,snail_rectangle)
        if self.position>=-100:
            self.position-=3
        else:
            del self


pygame.init()
screen = pygame.display.set_mode((800, 400))

#Imagenes
background_image = pygame.image.load("Rosendo\graphics\Sky.png").convert_alpha()
floor = pygame.image.load("Rosendo/graphics/ground.png").convert_alpha()
snail = pygame.image.load('Rosendo/graphics/snail/snail1.png').convert_alpha()
player_surface = pygame.image.load('Rosendo\graphics\Player\player_walk_1.png').convert_alpha()

#Configuraciones del juego
pygame.display.set_caption("Rosendo, Be Careful!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Rosendo/font/Pixeltype.ttf", 50)
pygame.display.set_icon(snail)
text_surface = test_font.render("START!", False, "Black")
text_rectangle = text_surface.get_rect(midbottom =(400,60))
player_gravity=300
seconds=round(pygame.time.get_ticks()/1000)


snails=[]
while True:
    # if close window is pressed the game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player_gravity-=20
    # Set the fixed objects
    pygame.display.update()
    screen.blit(background_image, [0, 0])
    screen.blit(floor, [0, 300])
    screen.blit(text_surface,text_rectangle)

    if random.random()>.995:
        snails.append(snailO())

    for i in snails:
        i.move()
    # Player
    player_rectangle = player_surface.get_rect(midbottom =(80,player_gravity))
    screen.blit(player_surface,player_rectangle)

    # Time
    seconds=round(pygame.time.get_ticks()/1000)
    if seconds<10:
        seconds="0"+str(seconds)
    time=test_font.render("Time:  "+str(seconds), False, "Black")
    time_rectangle = time.get_rect(topleft =(20,25))
    screen.blit(time,time_rectangle)

    clock.tick(60)


