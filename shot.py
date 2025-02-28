import pygame
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
    def draw(self, screen):
        # Draw an ellipse to represent the shot
        pygame.draw.ellipse(screen, (255, 180, 120), 
                            (self.position.x - self.radius, 
                             self.position.y - self.radius / 2, 
                             self.radius * 2, 
                             self.radius))
    def update(self, dt):
        self.position += self.velocity * dt
        
