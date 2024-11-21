import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, player):
        distance = self.position.distance_to(player.position)
        sum_radii = self.radius + player.radius
        return distance <= sum_radii
    
        #Core principles of OOP explained for this test project:

        #By putting the collision method in the parent class: 
        # All child classes get it automatically (Inheritance)
        # The logic is defined in one place (Encapsulation)
        # It works with any CircleShape object (Polymorphism)
