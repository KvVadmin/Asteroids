import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0) 
        # velocity = speed + direction. 
        # The shot needs a starting point = starting velocity which will then be updated when a shot is created

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
         
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += (forward * PLAYER_SPEED * dt )
         # Same orientation as player, same start as player, shoot speed = player. Moving shots with their own speed, not the one deinfed in parent class
    
