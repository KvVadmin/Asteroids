from player import Player
from circleshape import CircleShape
from constants import *
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    

    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    while True:
        dt = clock.tick(60)/1000
        print(f"dt: {dt}")  # get the time passed and update everything based on that new time (below methods)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()
  


