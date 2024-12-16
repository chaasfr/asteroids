import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)


    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for thing in updatables:
            thing.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                sys.exit('Game over!')

        screen.fill(color=(0,0,0))
        for thing in drawables:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()