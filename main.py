# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 

def main():
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")  
        pygame.init() # Initialize all imported pygame modules
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a GUI window with the specified dimensions
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return 
                screen.fill("black") #fills the screen with black color
                pygame.display.flip()  # Update the full display Surface to the screen --> must be called last in the loop
 

if __name__ == "__main__":
    main()
