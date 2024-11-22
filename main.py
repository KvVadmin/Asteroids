import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # creating groups/initialization code
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #assign containers and definining class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)
    
    #create an instance of Player class after assigning containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0
    

    #print("Starting asteroids!")
    #print("Screen width: 1280")
    #print("Screen height: 720")

  

    #gameloop
    while True:
        
        print(f"dt: {dt}")  # get the time passed and update everything based on that new time (below methods)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print ("Game over!")
                raise SystemExit 

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
  


