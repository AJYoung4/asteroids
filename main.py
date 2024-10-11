import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # set up pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0

    # Game Loop
    while True:
        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        for thing in asteroids:
            if thing.collision(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.collision(thing):
                    thing.split()
                    shot.kill()

        # fill the screen black
        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)

        # update the display
        pygame.display.flip()

        # set fps 60 and get delta time
        dt = clock.tick(60) / 1000 # convert milliseconds to seconds



if __name__ == '__main__':
    main()