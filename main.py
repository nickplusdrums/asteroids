import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *
import sys


def main():
    pygame.init()
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
            
        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for thing in asteroids:
            if thing.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        pygame.display.flip()

        dt = (clock.tick(60) / 1000)






if __name__ == "__main__":
    main()
