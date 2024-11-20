from player import Player
from constants import *
import pygame
def main ():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player = Player(640, 360 )
	
	
	while True:
		for event in pygame.event.get():
   			 if event.type == pygame.QUIT:
       				 return
		screen.fill((0,0,0))
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
	print ("Starting asteroids!")
	print ("Screen width: 1280")
	print ("Screen height: 720")






if __name__ == "__main__":
    main()
