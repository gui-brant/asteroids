#when the thing asks you to create a new class, it does imply that you should be making a new file too
from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen): #be more literal with the instructions. They say "Like Asteroid class in the sense that it used draw and update." Missed details because wanted to rush.
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 

    def update(self, dt): #be more literal with the instructions. They say "Like Asteroid class in the sense that it used draw and update." Missed details because wanted to rush.
        self.position += self.velocity * dt
    