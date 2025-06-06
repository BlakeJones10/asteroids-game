from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y,):
        self.velocity = pygame.Vector2(0, 0)
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt
