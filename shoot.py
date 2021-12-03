import random
import pgzrun
import pygame

my_actor=Actor('luis')
pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/song.mp3'))

def draw():
	screen.clear()
	my_actor.draw()

def place_my_actor(): 
	my_actor.x = random.randint(40,760)
	my_actor.y = random.randint(40,560)

def on_mouse_down(pos):
	if my_actor.collidepoint(pos):
		print("¡Buena puntería!") 
		place_my_actor()
	else:
		print("Te has equivocado")
		quit()


place_my_actor()
pgzrun.go()



