from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURNS_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
import pygame
from shot import Shot
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 0, 0), self.triangle())  # Fill with red
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)  # White border
    def rotate(self,dt):
        self.rotation += PLAYER_TURNS_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer >= 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        if self.timer <= 0:
            shot_velocity = pygame.Vector2(0, 1* PLAYER_SHOT_SPEED).rotate(self.rotation) 
            Shot(self.position, shot_velocity)
            self.timer = PLAYER_SHOT_COOLDOWN