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

    def collision(self, other): #other represents an object of the same class as self, but not self itself
        r1 = self.radius
        r2 = other.radius
        distance = r1 + r2
        if self.position.distance_to(other.position) < distance:
            return True
        else:
            return False
        #self.position is a pygame.Vector2() object, where pygame is a package or folder and Vector2() is a Class (arguments passed go into __init__)
        