import pygame
from constants import *
from player import *

def main():
    # set up pygame
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #player
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))


    # Game Loop
    while True:
        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        # fill the screen black
        screen.fill((0, 0, 0))
        
        # render player
        player.update(dt)
        player.draw(screen)

        # update the display
        pygame.display.flip()

        # set fps 60 and get delta time
        dt = clock.tick(60) / 1000 # convert milliseconds to seconds



if __name__ == '__main__':
    main()