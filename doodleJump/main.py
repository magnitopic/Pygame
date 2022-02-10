import pygame
import random as rnd
from sys import exit


class Leaf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("doodleJump/graphics/leaf.png").convert_alpha()


class Player:
    def __init__(self):
        self.x = 175
        self.y = 300
        self.dy = 0.0
        self.h = 200
        self.dead = 0
        self.normalImg = pygame.image.load("doodleJump/graphics/normal.png").convert_alpha()
        self.shootImg = pygame.image.load("doodleJump/graphics/shoot.png").convert_alpha()
        self.image = self.normalImg
        self.collisionBox = self.image.get_rect(topleft=(self.x, self.y))

    def movement(self, key):
        # if key is pressed and your x is not out of the screen,
        # move and cange image
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.x > 0:
            self.x -= 4
            self.image = self.normalImg
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.x < 270:
            self.x += 4
            self.image = pygame.transform.flip(self.normalImg, True, False)

    def jumping(self):
        self.dy += 0.2
        self.y += self.dy


class Monster:
    def __init__(self):
        self.x = rnd.randint(0, 230)
        self.y = 0
        self.direction = 1
        self.dead = True
        self.image = pygame.image.load("doodleJump/graphics/monster.png").convert_alpha()
        self.collisionBox = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)


class Projectile:
    def __init__(self, x=0, y=0):
        self.cooldown = 1
        self.x = x
        self.y = y
        self.image = pygame.image.load("doodleJump/graphics/projectile.png").convert_alpha()
        self.collisionBox = self.image.get_rect(topleft=(self.x, self.y))


class Game:
    def __init__(self):
        # we start the game
        pygame.init()
        # game settings
        self.screen = pygame.display.set_mode((350, 600))
        self.clock = pygame.time.Clock()
        self.startGame()
        pygame.display.set_caption("Doodle jump")
        pygame.display.set_icon(self.player.image)

        # variables
        self.key = pygame.key.get_pressed()
        self.background = pygame.image.load("doodleJump/graphics/background.jpg").convert_alpha()
        self.monsterPoints=rnd.randrange(60,80)
        # Fonts
        pygame.font.init()
        self.pointsFont = pygame.font.SysFont("comicsans", 20)
        self.gameOverFont = pygame.font.SysFont("Verdana", 30)

    def startGame(self):
        self.points = 0
        self.player = Player()
        self.monster = None
        self.leafs = [Leaf(rnd.randrange(0, 270), rnd.randrange(0, 600))for i in range(14)]
        self.projectile = Projectile()
        # Music
        pygame.mixer.pause()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('doodleJump/audio/main.wav'), -1)
        # pygame.mixer.Channel(0).set_volume(0)

    def dead(self):
        self.screen.fill("red")
        text = self.gameOverFont.render("Game Over...", 1, (0, 0, 0))
        self.screen.blit(text, (75, 200))
        text = self.gameOverFont.render(f"Your score: {self.points} points", 1, (0, 0, 0))
        self.screen.blit(text, (40, 300))
        text = self.gameOverFont.render(f"Space to play again", 1, (0, 0, 0))
        self.screen.blit(text, (40, 400))
        if self.key[pygame.K_SPACE]:
            self.startGame()

    def deadSound(self):
        pygame.mixer.pause()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('doodleJump/audio/death.mp3'))

    # main program

    def main(self):
        while True:
            # if close window button is pressed the game closes
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # get new key
            self.key = pygame.key.get_pressed()
            if self.player.dead:
                self.dead()
            else:
                # Draw repeating background
                for x in range(0, 350, 339):
                    for y in range(0, 600, 509):
                        self.screen.blit(self.background, (x, y))
                # update player.collisionBox to players position
                self.player.collisionBox = self.player.image.get_rect(
                    topleft=(self.player.x, self.player.y))

                # Player movement
                self.player.movement(self.key)

                # Setting the leafs
                for leaf in self.leafs:
                    self.screen.blit(leaf.image, (leaf.x, leaf.y))

                # Going up
                if self.player.y < self.player.h:
                    self.player.y = self.player.h
                    # move the leafs
                    for leaf in self.leafs:
                        leaf.y -= self.player.dy
                        if leaf.y > 600:
                            leaf.y = 0
                            leaf.x = rnd.randrange(0, 270)
                            self.points += 1
                    # spawn monster
                    if self.points % self.monsterPoints == 0 and self.points > 1 and self.monster == None:
                        self.monster = Monster()

                # player Jumping
                self.player.jumping()

                # player dying
                if self.player.y > 600:
                    self.deadSound()
                    self.player.dead = True

                # shooting and drawing player
                if self.key[pygame.K_SPACE] or self.key[pygame.K_UP]:
                    self.screen.blit(self.player.shootImg,self.player.collisionBox)
                    if self.projectile.cooldown <= 0:
                        self.projectile = Projectile(self.player.x + 20, self.player.y)
                else:
                    self.screen.blit(self.player.image,self.player.collisionBox)
                # projectile logic
                self.projectile.cooldown -= 0.02
                self.projectile.y -= 7
                self.projectile.collisionBox = self.projectile.image.get_rect(topleft=(self.projectile.x, self.projectile.y))
                self.screen.blit(self.projectile.image,self.projectile.collisionBox)
                

                # draw points
                text = self.pointsFont.render(f"Points: {self.points}", 1, (0, 0, 0))
                self.screen.blit(text, (220, 10))

                # Colition with leafs
                for leaf in self.leafs:
                    if (self.player.x + 50 > leaf.x) and (self.player.x + 20 < leaf.x + 68) and (self.player.y + 70 > leaf.y) and (self.player.y + 70 < leaf.y + 14) and self.player.dy > 0:
                        self.player.dy = -10

                # monster logic
                if not self.monster == None:
                    # update monster.collisionBox to monsters position
                    self.monster.collisionBox = self.monster.image.get_rect(topleft=(self.monster.x, self.monster.y))

                    # movement
                    # Move monster down when player moves up
                    if self.player.y < self.player.h:
                        self.monster.y -= self.player.dy
                    # Move monster depending on the direction
                    if self.monster.direction:
                        self.monster.x += 1.5
                    else:
                        self.monster.x -= 1.5
                    # Change monster direction
                    if self.monster.x >= 230:
                        self.monster.direction = 0
                    elif self.monster.x <= 0:
                        self.monster.direction = 1
                    # draw monster
                    self.screen.blit(self.monster.image,self.monster.collisionBox)

                    # deaths
                    # if monster colides with player, player dies
                    if self.player.collisionBox.colliderect(self.monster.collisionBox):
                        self.deadSound()
                        self.player.dead = True
                    # if projectile hits monster he dies
                    if self.monster.collisionBox.colliderect(self.projectile.collisionBox):
                        self.monster = None
                    # if monster goes bellow the screen, he dies
                    elif self.monster.y > 600:
                        self.monster = None
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.main()
