import pygame
import time
import random

# measures,distance...
screen_width = 606
screen_height = 606
distance = 2


# game state
start = 1
playing = 2
game_over = 3
game_state = playing


# score atributes
score = 0
scoreX = 390
scoreY = 10
pygame.font.init()
scoreFont = pygame.font.Font("fonts/Emulogic-zrEw.ttf", 15)
introFont = pygame.font.Font("fonts/Pacfont-ZEBZ.ttf", 50)


# initialize the screen
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PA C- MAN")


# images
background_image = pygame.image.load('images/background_image.png').convert()
img = pygame.image.load("images/walk.png").convert()


# icon game
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set the game clock
clock = pygame.time.Clock()


# groups
wall_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()


# walls class
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, width, height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


# walls for the game
walls = [[0, 0, 6, 600],
         [0, 0, 600, 6],
         [0, 600, 606, 6],
         [600, 0, 6, 606],
         [300, 0, 6, 66],
         [60, 60, 186, 6],
         [360, 60, 186, 6],
         [60, 120, 66, 6],
         [60, 120, 6, 126],
         [180, 120, 246, 6],
         [300, 120, 6, 66],
         [480, 120, 66, 6],
         [540, 120, 6, 126],
         [120, 180, 126, 6],
         [120, 180, 6, 126],
         [360, 180, 126, 6],
         [480, 180, 6, 126],
         [180, 240, 6, 126],
         [180, 360, 246, 6],
         [420, 240, 6, 126],
         [240, 240, 42, 6],
         [324, 240, 42, 6],
         [240, 240, 6, 66],
         [240, 300, 126, 6],
         [360, 240, 6, 66],
         [0, 300, 66, 6],
         [540, 300, 66, 6],
         [60, 360, 66, 6],
         [60, 360, 6, 186],
         [480, 360, 66, 6],
         [540, 360, 6, 186],
         [120, 420, 366, 6],
         [120, 420, 6, 66],
         [480, 420, 6, 66],
         [180, 480, 246, 6],
         [300, 480, 6, 66],
         [120, 540, 126, 6],
         [360, 540, 126, 6]
         ]


# create the list that contain all the objects that means wall in the game and posicionate the walls in the screen
for item in walls:
    wall = Wall(item[0], item[1], item[2], item[3], BLUE)
    wall_list.add(wall)
    all_sprites_list.add(wall)


# the white gate for the ghost spawn
gate = pygame.sprite.Group()
gate.add(Wall(282, 242, 42, 2, WHITE))
all_sprites_list.add(gate)


# the balls pacman wants to eat
balls_list = pygame.sprite.Group()


class Balls(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.imageSource = pygame.image.load('images/ball.png').convert_alpha()
        self.image = pygame.transform.scale(self.imageSource, (10, 10))

        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.top = x
        self.rect.left = y


# create the balls in the map
balls = [Balls(x, y) for x in range(30, 600, 60)
         for y in range(30, 600, 60) if not (180 < x < 360 and 180 < y < 420)]
balls_list.add(balls)


# player class
class Player:
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.x = screen_width / 2 - 15
        self.y = screen_height / 2 + 74
        self.imageSource = pygame.image.load(
            'images/player.png').convert_alpha()
        self.image = self.imageSource
        self.lives = 3
        self.alive = True
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.direction = 3

    # movement for pacman
    def move(self, distance):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.x += distance
            self.direction = 3
            self.image = pygame.transform.rotate(self.imageSource, 360)
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.x -= distance
            self.direction = 2
            self.image = pygame.transform.rotate(self.imageSource, 180)
        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.y -= distance
            self.direction = 1
            self.image = pygame.transform.rotate(self.imageSource, 90)
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.y += distance
            self.direction = 4
            self.image = pygame.transform.rotate(self.imageSource, 270)
        elif key[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    def draw(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

class Ghost():
    def __init__():
        pass

# create Pacman player
player = Player()


# logic of the game

# main menu
screen.fill(BLACK)

# Intro music and text
screen.blit(scoreFont.render(f"pacman", 1, (255, 255, 255)), (10, 10))
song=pygame.mixer.Sound("sounds/intro.wav")
song.play()
time.sleep(song.get_length()+.5)


# game running
while game_state == playing:
    # if close window is pressed the game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # check if pacman hits a wall------------- to do---------------------------(esto se carga lo que hay en la lista cuidao)
    gets_hit = pygame.sprite.spritecollide(player, balls_list, True)
    if gets_hit != []:
        score += 1
    text = scoreFont.render(f"Your score: {score}", 1, (255, 255, 255))
    screen.blit(text, (scoreX, scoreY))
    # score's position
    if player.x>300 and player.y <100:
        scoreX=scoreY=10
    else:
        scoreX,scoreY=390,10

    #gets_hit = pygame.sprite.spritecollide(player, wall_list, True)
    #gets_hit = pygame.sprite.collide_rect(player.rect)
    # if player == gets_hit:
    #    print("muro")

    # update the window
    pygame.display.update()
    screen.fill(BLACK)
    wall_list.draw(screen)
    gate.draw(screen)
    balls_list.draw(screen)

    # colition for pacman
    colition_pacman = any([True if player.rect.colliderect(wall.rect) else False for wall in wall_list])
    
    colition_gate = any([True if player.rect.colliderect(gate.rect) else False for gate in gate])

    if colition_pacman and player.direction == 3:
        player.x -= distance
    if colition_pacman and player.direction == 2:
        player.x += distance
    if colition_pacman and player.direction == 1:
        player.y += distance
    if colition_pacman and player.direction == 4:
        player.y -= distance
    if colition_gate and player.direction == 4:
        player.y -= distance

    player.move(distance)
    player.draw()
    clock.tick(60)
