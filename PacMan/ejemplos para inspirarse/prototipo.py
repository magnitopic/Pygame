import pygame
import random

#-----screen size-----#
screen_width = 800
screen_height = 650


# iniciamos la pantalla
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # esto es para crear el objeto jugador y sus propiedades (x,y...)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        img = pygame.image.load("walk.png").convert()

        #--------------𝗰𝗵𝗲𝘁𝗮𝗼--------------#
        # Create the animations objects Ll ⁡⁢⁣⁢⁡⁢⁣⁢
        self.move_right_animation = Animation(img, 32, 32)
        self.move_left_animation = Animation(
            pygame.transform.flip(img, True, False), 32, 32)
        self.move_up_animation = Animation(
            pygame.transform.rotate(img, 90), 32, 32)
        self.move_down_animation = Animation(
            pygame.transform.rotate(img, 270), 32, 32)
        # Load explosion image
        img = pygame.image.load("explosion.png").convert()
        self.explosion_animation = Animation(img, 30, 30)
        # Save the player image
        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey(BLACK)



        #chetadísimo, esto es para saber si puedes moverte hacia un lado o otro (en plan el mapa de 0,1,2 y 3)
        def update(self, horizontal_blocks, vertical_blocks):
            if not self.explosion:
                if self.rect.right < 0:
                    self.rect.left = SCREEN_WIDTH
                elif self.rect.left > SCREEN_WIDTH:
                    self.rect.right = 0
                if self.rect.bottom < 0:
                    self.rect.top = SCREEN_HEIGHT
                elif self.rect.top > SCREEN_HEIGHT:
                    self.rect.bottom = 0
                self.rect.x += self.change_x
                self.rect.y += self.change_y




class Animation(object):
    def __init__(self,img,width,height):
        # Load the sprite sheet
        self.sprite_sheet = img
        # Create a list to store the images
        self.image_list = []
        self.load_images(width,height)
        # Create a variable which will hold the current image of the list
        self.index = 0
        # Create a variable that will hold the time
        self.clock = 1
        
    def load_images(self,width,height):
        # Go through every single image in the sprite sheet
        for y in range(0,self.sprite_sheet.get_height(),height):
            for x in range(0,self.sprite_sheet.get_width(),width): 
                # load images into a list
                img = self.get_image(x,y,width,height)
                self.image_list.append(img)

    def get_image(self,x,y,width,height):
        # Create a new blank image
        image = pygame.Surface([width,height]).convert()
        # Copy the sprite from the large sheet onto the smaller
        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        # Assuming black works as the transparent color
        image.set_colorkey((0,0,0))
        # Return the image
        return image

    def get_current_image(self):
        return self.image_list[self.index]

    def get_length(self):
        return len(self.image_list)

    def update(self,fps=30):
        step = 30 // fps
        l = range(1,30,step)
        if self.clock == 30:
            self.clock = 1
        else:
            self.clock += 1

        if self.clock in l:
            # Increase index
            self.index += 1
            if self.index == len(self.image_list):
                self.index = 0
