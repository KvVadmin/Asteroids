import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.timer > 0:
            return
        #create a shot at the player's current position
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot_position = self.position
        shot = Shot(shot_position.x, shot_position.y)
            
        #defining direction and velocity of the shot
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        


    

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:        
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    
    def rotate(self, dt):
        rotation_amount = PLAYER_TURN_SPEED * dt
        self.rotation += rotation_amount
    
    def move(self, dt):
        #player's rotation/direction and speed
        forward = pygame.Vector2(0, 1).rotate(self.rotation) 
        self.position += forward * PLAYER_SPEED * dt   

