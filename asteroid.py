import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
       
        pygame.draw.circle (screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
       self.move(dt)
        
    
    def move(self, dt):
        self.position += self.velocity * dt

    def collision(self, OtherCircleShape):
        distance = pygame.math.Vector2.distance_to(self.position, OtherCircleShape.position)
        sum_radii = self.radius + OtherCircleShape.radius
        return distance <= sum_radii


        
        