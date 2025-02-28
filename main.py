import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 70))


        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
