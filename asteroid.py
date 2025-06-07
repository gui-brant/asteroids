import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius) #said "the class should inherit from CircleShape" and you forgot to actually inherit
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2) #this was a bit confusing to be fair
    
    def update(self, dt):
        self.position += self.velocity * dt

    