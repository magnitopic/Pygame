import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((350, 600))

# Images
background = pygame.image.load(
    "doodleJump/graphics/background.jpg").convert_alpha()
playerImage = pygame.image.load(
    "doodleJump/graphics/normal.png").convert_alpha()
playerShoot = pygame.image.load(
    "doodleJump/graphics/shoot.png").convert_alpha()
leafImage = pygame.image.load("doodleJump/graphics/leaf.png").convert_alpha()
monsterImage = pygame.image.load(
    "doodleJump/graphics/monster.png").convert_alpha()

# Pygame configs
clock = pygame.time.Clock()
pygame.display.set_caption("Doodle jump")
pygame.display.set_icon(playerImage)
pygame.font.init()
pointsFont = pygame.font.SysFont("comicsans", 20)
gameOverFont = pygame.font.SysFont("Verdana", 30)

# Music
pygame.mixer.Channel(0).play(
    pygame.mixer.Sound('doodleJump/audio/main.wav'), -1)
pygame.mixer.Channel(0).set_volume(0)

# Object instantiating


class Leaf:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Player:
    def __init__(self):
        self.x = 175
        self.y = 300
        self.dy = 0.0
        self.h = 200
        self.dead = 0


class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 1
        self.speed = random.randint(1, 2)


def startGame():
    global player
    global leafs
    player = Player()
    leafs = [Leaf(random.randrange(0, 270), random.randrange(0, 600))
             for i in range(14)]
    screen.blit(leafImage, (player.x, player.y+20))
    global points
    global monster
    points = 0
    monster = ""


startGame()
while True:
    key = pygame.key.get_pressed()
    playerRectange = playerImage.get_rect(topleft=(player.x, player.y))
    # if close window button is pressed the game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if player.dead:
        pygame.mixer.pause()
        screen.fill("red")
        text = gameOverFont.render("Game Over...", 1, (0, 0, 0))
        screen.blit(text, (70, 200))
        text = gameOverFont.render(f"Score: {points} points", 1, (0, 0, 0))
        screen.blit(text, (40, 350))
        if key[pygame.K_SPACE]:
            startGame()
    else:
        # Draw repeating background
        for x in range(0, 350, 339):
            for y in range(0, 600, 509):
                screen.blit(background, (x, y))

        # Player movement
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and player.x > 0:
            player.x -= 4
            player.y -= 0.5
            playerImage = pygame.image.load("doodleJump/graphics/normal.png")
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and player.x < 270:
            player.x += 4
            player.y += .5
            playerImage = pygame.transform.flip(pygame.image.load(
                "doodleJump/graphics/normal.png"), True, False)

        # Setting the leafs
        for leaf in leafs:
            screen.blit(leafImage, (leaf.x, leaf.y))

        # Going up
        if player.y < player.h:
            player.y = player.h
            for leaf in leafs:
                leaf.y -= player.dy
                if leaf.y > 600:
                    leaf.y = 0
                    leaf.x = random.randrange(0, 270)
                    points += 1
                if points % 75 == 0 and points > 1 and monster == "":
                    monster = Monster(random.randint(1, 230), 2)

        # player Jumping
        player.dy += 0.2
        player.y += player.dy

        # player dying
        if player.y > 600:
            player.dead = True

        # shooting
        if key[pygame.K_SPACE] or key[pygame.K_UP]:
            screen.blit(playerShoot, [player.x, player.y])
        else:
            screen.blit(playerImage, playerRectange)

        # draw points
        text = pointsFont.render("Points: " + str(points), 1, (0, 0, 0))
        screen.blit(text, (220, 10))

        # Colition with leafs
        for leaf in leafs:
            if (player.x + 50 > leaf.x) and (player.x + 20 < leaf.x + 68) and (player.y + 70 > leaf.y) and (player.y + 70 < leaf.y + 14) and player.dy > 0:
                player.dy = -10

        # monster display
        if monster != '':
            monsterRectange = monsterImage.get_rect(
                topleft=(monster.x, monster.y))
            if playerRectange.colliderect(monsterRectange):
                player.dead = True
            # Move monster down when player moves up
            if player.y < player.h:
                monster.y -= player.dy
            # Move monster depending on the direction
            if monster.direction:
                monster.x += monster.speed
            else:
                monster.x -= monster.speed
            # Change monster direction
            if monster.x >= 230:
                monster.direction = 0
            elif monster.x <= 0:
                monster.direction = 1
            # draw monser
            screen.blit(monsterImage, monsterRectange)
            if monster.y > 600:
                monster = ""

    pygame.display.update()
    clock.tick(60)
