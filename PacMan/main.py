import pygame
import time
import random

random.seed()

# measures,distance...
screen_width = 606
screen_height = 606
distance = 2
up = 0
left = 1
right = 2
down = 3






# game state
game_state = "playing"


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
RED = (255, 0, 0)

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

angles = [
        [6, 28,67,87,right],
        [126,148,67,87,down],
        [246,268,67,87,up],
        [306,328,67,87,up],
        [426,448,67,87,down],
        [546,568,67,87,left],

        [126,148,127,147,up],
        [246,448,127,147,up],

        [186,208,187,207,down],
        [246,448,187,207,up],
        [306,328,187,207,up],
        [366,388,187,207,down],

        [66,88,247,267,left],
        [486,508,247,267,right],

        [66,88,307,327,up],
        [126,148,307,327,left],
        [426,448,307,327,right],
        [486,508,307,327,up],

        [126,248,367,387,up],
        [426,448,367,387,up],

        [66,88,487,507,right],
        [126,148,487,507,up],
        [426,448,487,507,up],
        [486,508,487,507,left],

        [66,88,547,567,up],
        [246,448,547,567,up],
        [306,328,547,567,up],
        [486,508,547,567,up]]

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
balls = [Balls(x, y) for x in range(30, 600, 60)for y in range(
    30, 600, 60) if not (180 < x < 360 and 180 < y < 420)]
balls_list.add(balls)


# player class
class Player(pygame.sprite.Sprite):
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
        self.direction = 2

    # movement for pacman
    def move(self, distance, key):
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.x += distance
            self.direction = 2
            self.image = pygame.transform.rotate(self.imageSource, 360)

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.x -= distance
            self.direction = 1
            self.image = pygame.transform.rotate(self.imageSource, 180)

        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.y -= distance
            self.direction = 0
            self.image = pygame.transform.rotate(self.imageSource, 90)

        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.y += distance
            self.direction = 3
            self.image = pygame.transform.rotate(self.imageSource, 270)

    def draw(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)


class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = screen_width / 2 - 15
        self.y = screen_height / 2 - 45
        self.image = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost.png').convert_alpha(), size=(32, 32))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.direction = 0
        self.distance = 2
        self.collide = False
        self.colition = False
        self.in_angle = False
        self.angle_regist = False
        self.angle_changed = True

    def changeDirection(self):
        self.direction = (random.randint(1, 3)+self.direction) % 4

    def move(self, ghost_distance):

        if self.direction == 0:
            self.y -= ghost_distance

        if self.direction == 1:
            self.x -= ghost_distance

        if self.direction == 2:
            self.x += ghost_distance

        if self.direction == 3:
            self.y += ghost_distance

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def draw(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def avoid_top(self):
        self.y += self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def avoid_left(self):
        self.x += self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def avoid_right(self):
        self.x -= self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def avoid_bottom(self):
        self.y -= self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)


    def angle_up(self):
        if self.direction == left:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = left

        if self.direction == right:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = right

        if self.direction == down:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = right

            elif angleDirection == 2:
                self.direction = down


    def angle_left(self):
        if self.direction == down:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = left

        if self.direction == up:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = left

        if self.direction == right:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = right

            elif angleDirection == 2:
                self.direction = down


    def angle_right(self):
        if self.direction == up:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = right

        if self.direction == down:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = right

        if self.direction == left:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = up

            elif angleDirection == 2:
                self.direction = down


    def angle_down(self):
        if self.direction == left:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = left

        if self.direction == right:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = right

        if self.direction == up:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = right

            elif angleDirection == 2:
                self.direction = up


# create Pacman player
player = Player()


# the ghosts that want to eat pacman
ghost1 =  Ghost()
ghost2 =  Ghost()
ghost3 =  Ghost()
ghost4 =  Ghost()
ghosts = [ghost1,
          ghost2,
          ghost3,
          ghost4
          ]


# logic of the game
# main menu
screen.fill(BLACK)

# Intro music and text
screen.blit(scoreFont.render("pacman", 1, (255, 255, 255)), (255, 300))
pygame.display.update()
song = pygame.mixer.Sound("sounds/intro.wav")
song.play()
time.sleep(song.get_length()+.5)


# game running
while True:
    # if close window is pressed the game closes
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    if game_state == "game_over":
        screen.fill(BLACK)
        screen.blit(scoreFont.render("GAME_OVER", 1, (RED)), (255, 300))
        pygame.display.update()

    elif game_state == "game_ended":
        screen.fill(BLACK)
        screen.blit(scoreFont.render("You win :D", 1, (WHITE)), (255, 300))
        pygame.display.update()

    else:
        # check if pacman hits a wall------------- to do---------------------------(esto se carga lo que hay en la lista cuidao)
        gets_hit = pygame.sprite.spritecollide(player, balls_list, True)
        if gets_hit != []:
            score += 1
        # draw score
        text = scoreFont.render(f"Your score: {score}", 1, (255, 255, 255))
        screen.blit(text, (scoreX, scoreY))
        # score's position
        if player.x > 300 and player.y < 100:
            scoreX = scoreY = 10
        else:
            scoreX, scoreY = 390, 10

        # update the window
        pygame.display.update()
        screen.fill(BLACK)
        wall_list.draw(screen)
        gate.draw(screen)
        balls_list.draw(screen)

        # colition for pacman
        pacman_colition = any([True if player.rect.colliderect(
            wall.rect) else False for wall in wall_list])
        pacman_colition_gate = any(
            [True if player.rect.colliderect(gate.rect) else False for gate in gate])

        if pacman_colition and player.direction == 0:
            player.y += distance

        if pacman_colition and player.direction == 1:
            player.x += distance

        if pacman_colition and player.direction == 2:
            player.x -= distance

        if pacman_colition and player.direction == 3:
            player.y -= distance

        if pacman_colition_gate and player.direction == 3:
            player.y -= distance

        player.move(distance, key)
        player.draw()
        #------ghost movement------#
        for item in ghosts:

            for wall in wall_list:
                item.collide = pygame.Rect.colliderect(item.rect, wall.rect)
                if item.collide:
                    break

            if not item.collide and item.colition == False:
                #print("no no")
                item.move(item.distance)
            elif item.collide and item.colition == False:
                #print("si no")
                item.colition = True
                item.draw()

            elif item.collide and item.colition == True:
                #print("si si")
                if item.direction == 0:
                    item.avoid_top()

                if item.direction == 1: 
                    item.avoid_left()

                if item.direction == 2:
                    item.avoid_right()

                if item.direction == 3:
                    item.avoid_bottom()

            elif not item.collide and item.colition == True:
                #print("no si")
                item.colition = False
                item.changeDirection()
                item.move(item.distance)

            #ghost_colition = any([True if ghost.rect.colliderect(wall.rect) else False for wall in wall_list])
            # ghost.changeDirection(ghost_colition)

            
            for value in angles:
                if value[0] <= (item.x +1) and value[1] >= (item.x-1) and value[2] <= (item.y+1) and value[3] >= (item.y-1):
                    item.in_angle = True
                    break
                else:
                    item.in_angle = False

            if not item.in_angle and item.angle_regist == False:
                print("no no")

            elif item.in_angle and item.angle_regist == False:
                print("si no")
                item.angle_regist = True

            elif item.in_angle and item.angle_regist == True and item.angle_changed == False:
                print("si si no")
                if value[4] == up:
                    item.angle_up()
                    print("up")

                elif value[4] == left:
                    item.angle_left()
                    print("left")

                elif value[4] == right:
                    item.angle_right()
                    print("right")

                elif value[4] == up:
                    item.angle_down()
                    print("down")

                item.angle_changed = True
            
            elif item.in_angle and item.angle_regist == True and item.angle_changed == True:
                pass

            elif not item.in_angle and item.angle_regist == True:
                print("no si")
                item.angle_regist = False
                item.angle_changed = False

            if item.rect.colliderect(player.rect):
                game_state = "game_over"
            elif score == 88:
                game_state = "game_ended"
        
        ejes = scoreFont.render(f"X: {player.x}, Y: {player.y}", 1, (255, 255, 255))
        screen.blit(ejes, (30, 580))

    clock.tick(60)
