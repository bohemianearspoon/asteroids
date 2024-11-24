import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        plus_angle = self.velocity.rotate(random_angle)
        minus_angle = self.velocity.rotate(0 - random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        plus_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        minus_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        plus_asteroid.velocity = plus_angle * 1.2
        minus_asteroid.velocity = minus_angle * 1.2


            
        
        

    