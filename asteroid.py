from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, random.randint(0, 255)), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            for _ in range(2):
                new_radius = self.radius - ASTEROID_MIN_RADIUS
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_velocity = self.velocity *1.2
                asteroid.velocity = new_velocity.rotate(random.uniform(20, 50))
