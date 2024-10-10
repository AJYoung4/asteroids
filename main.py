import pygame
from constants import *

def main():
    # set up pygame
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game Loop
    while True:
        
        # fill the screen black
        screen.fill((0, 0, 0))
        
        # update the display
        pygame.display.flip()



if __name__ == '__main__':
    main()