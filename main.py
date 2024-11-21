import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #assign containers
    Player.containers = (updatable, drawable)
    #create player after assigning containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    

    #print("Starting asteroids!")
    #print("Screen width: 1280")
    #print("Screen height: 720")

  

    
    while True:
        
        print(f"dt: {dt}")  # get the time passed and update everything based on that new time (below methods)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
  


