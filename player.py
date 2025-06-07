#You're looking too much at the answer key. This has happened enough times now. If you lose your patience again, you're out of this module. 
from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape): #don't forget your "self."s
    def __init__(self, x, y): 
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 #don't forget your "self."s
        self.timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
        self.timer -= dt 
        self.move(dt)
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0 :
            return
        shot = Shot(self.position.x, self.position.y) #x and y are never explicitly defined. They are defined through the position field (an object of Vector2, who contains x and y, in CircleShape's constructor)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED #the pygame.Vectory2() has a method called rotate(); we just redefine it on the Player() class
        #Note: self.rotation is the player's current facing direction. It changes as the player moves! Therefore, rotate(self.rotation) means: rotate with the player, which you were confused about





        


