# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")  
        pygame.init() # Initialize all imported pygame modules
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a GUI window with the specified dimensions
        clock = pygame.time.Clock()  # Create a clock object to control the frame rate
        dt = 0  # Initialize delta time variable
        updatables = pygame.sprite.Group() #creates the updatable group for different functionalities
        drawables = pygame.sprite.Group()  #creates the drawable group for different functionalities
        Player.containers = (updatables, drawables) #setting the two groups above as containers for the Player class
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # Create a player object at the center of the screen

        #This is pertain to asteroids stuff:
        asteroids = pygame.sprite.Group() #creates the a group for the asteroid objects
        Asteroid.containers = (asteroids, updatables, drawables) #this adds Asteroid objects as part of updatables, drawables, and asteroids. So whenever updatables is called in main(), the AsteroidField sprite will also be called with Asteroid and Player objects

        AsteroidField.containers = updatables #This adds AsteroidField objects as part of updatables. So whenever updatables is called in main(), the AsteroidField sprite will also be called with Asteroid and Player objects
        asteroid_field = AsteroidField()
        # Main game loop
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return 
                screen.fill("black") #fills the screen with black color

                updatables.update(dt)
                for asteroid in asteroids:
                       if asteroid.collision(player) == True:
                              print("Game over!")
                              sys.exit()
                for drawable in drawables:
                       drawable.draw(screen)     
                
                dt = clock.tick(60)/1000 # .tick() returns the number of milliseconds since the last call, so we divide by 1000 to get seconds, meaning the time for 1/60th of a second, or a frame
                pygame.display.flip()  # Update the full display Surface to the screen --> must be called last in the loop
                
                



if __name__ == "__main__":
    main()
