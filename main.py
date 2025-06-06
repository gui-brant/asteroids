# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import Player

def main():
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")  
        pygame.init() # Initialize all imported pygame modules
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a GUI window with the specified dimensions
        pygame.time.Clock()  # Create a clock object to control the frame rate
        dt = 0  # Initialize delta time variable
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # Create a player object at the center of the screen
        # Main game loop
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return 
                screen.fill("black") #fills the screen with black color
                player.draw(screen) #the player has to pop up after the screen pops up but before the frame is refreshed
                player.update(dt)  # Update the player object with the current delta time
                dt = pygame.time.Clock().tick(60)/1000 # .tick() returns the number of milliseconds since the last call, so we divide by 1000 to get seconds, meaning the time for 1/60th of a second, or a frame
                pygame.display.flip()  # Update the full display Surface to the screen --> must be called last in the loop
                
                



if __name__ == "__main__":
    main()
