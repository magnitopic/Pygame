import random
import pgzrun
import pygame

puntos=0
screen = pygame.display.set_mode((350, 600))
x1=Actor('x')
x2=Actor('x')
name=input("Cual es tu nombre?: ") or "player1"
print("Elige a quien disparar.\n1 <- Alien\n2 <- apple\n3 <- luis")
actor=input("Tu respuesta: ")
if actor != "1" and actor != "2" and actor != "3":
	actor="3"
if actor=="1":
	my_actor=Actor('alien')
elif actor=="2":
	my_actor=Actor('apple')
else:
	my_actor=Actor('luis')


pygame.mixer.Channel(0).play(pygame.mixer.Sound('shootGame/sounds/song.mp3'))
pygame.mixer.Channel(0).set_volume(0.5)
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
background_image = pygame.image.load("shootGame/images/background.png").convert()

def draw():
	screen.clear()
	screen.blit(background_image, [0, 0])
	my_actor.draw()
	x1.draw()
	x2.draw()

def place_my_actor(): 
	my_actor.x = random.randint(40,760)
	my_actor.y = random.randint(40,560)
	x1.x = 40
	x1.y = 40
	x2.x = 90
	x2.y = 40

def on_mouse_down(pos):
	global puntos
	if my_actor.collidepoint(pos):
		puntos+=1
		print(f"¡Buena puntería! Tienes {puntos} puntos")
		if random.random() < .5:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound('shootGame/sounds/shot_a.mp3'))
		else:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound('shootGame/sounds/shot_b.mp3'))
		place_my_actor()
	else:
		print("Te has equivocado")
		quit()
	

place_my_actor()
pgzrun.go()
