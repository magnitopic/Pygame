import pygame, random
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
screen_w, screen_h = screen.get_size()
image_w, image_h = background.get_size()

# Pygame configs
clock = pygame.time.Clock()
pygame.display.set_caption("Doodle jump")
pygame.display.set_icon(playerImage)
pygame.font.init()
pointsFont = pygame.font.SysFont("comicsans", 20)
gameOverFont = pygame.font.SysFont("Verdana", 30)


# Object instantiating
class Leaf:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        leaf_rectangle = leafImage.get_rect(midbottom=(self.x, self.y))
        screen.blit(leafImage, leaf_rectangle)


class Player:
    x = 175
    y = 300
    dy = 0.0
    h = 200

    def draw(self):
        player_rectangle = leafImage.get_rect(midbottom=(self.x, self.y))
        screen.blit(leafImage, player_rectangle)


# Creating objects
doodle = Player()
leafs = [Leaf(random.randrange(0, 270), random.randrange(0, 600))
         for i in range(15)]
points = 0
while True:
    # if close window button is pressed the game closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw repeating background
    for x in range(0, screen_w, image_w):
        for y in range(0, screen_h, image_h):
            screen.blit(background, (x, y))

    # Player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and doodle.x > 0:
        doodle.x -= 4
        playerImage = pygame.image.load("doodleJump/graphics/normal.png")
    if key[pygame.K_RIGHT] and doodle.x < 270:
        doodle.x += 4
        playerImage = pygame.transform.flip(pygame.image.load(
            "doodleJump/graphics/normal.png"), True, False)

    # Setting the leafs
    for leaf in leafs:
        screen.blit(leafImage, (leaf.x, leaf.y))

    # Going up
    if doodle.y < doodle.h:
        doodle.y = doodle.h
        for leaf in leafs:
            leaf.y -= doodle.dy
            if leaf.y > 600:
                leaf.y = 0
                leaf.x = random.randrange(0, 270)
                points += 1

    # Jumping
    doodle.dy += 0.2
    doodle.y += doodle.dy
    if doodle.y > 600:
        screen.fill("red")
        text = gameOverFont.render("Game Over...", 1, (0, 0, 0))
        screen.blit(text, (70, 200))
    else:
        # if game not over draw points
        text = pointsFont.render("Points: " + str(points), 1, (0, 0, 0))
        screen.blit(text, (220, 10))

    # Colition with leafs
    for leaf in leafs:
        if (doodle.x + 50 > leaf.x) and (doodle.x + 20 < leaf.x + 68) and (doodle.y + 70 > leaf.y) and (doodle.y + 70 < leaf.y + 14) and doodle.dy > 0:
            doodle.dy = -10

    # Draw player
    if key[pygame.K_UP]:
        screen.blit(playerShoot, [doodle.x, doodle.y])
    else:
        screen.blit(playerImage, [doodle.x, doodle.y])

    pygame.display.update()
    clock.tick(60)
