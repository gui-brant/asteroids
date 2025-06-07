import pygame
from circleshape import *
from constants import *
import random
#from player.py import rotate
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius) #said "the class should inherit from CircleShape" and you forgot to actually inherit
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2) #this was a bit confusing to be fair
    
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            neg_random_angle = random_angle * -1
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(neg_random_angle)
            smaller_ast_rad = self.radius - ASTEROID_MIN_RADIUS
            smaller_ast1 = Asteroid(self.position.x, self.position.y, smaller_ast_rad)
            smaller_ast1.velocity = velocity1 *1.2
            smaller_ast2 = Asteroid(self.position.x, self.position.y, smaller_ast_rad)
            smaller_ast2.velocity = velocity2 *1.2
            return smaller_ast1, smaller_ast2

    