from circleshape import *
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        rand_num = random.uniform(20, 50)
        new_velocity_vector = self.position.rotate(rand_num)
        new_velocity_vector2 = self.position.rotate(-rand_num)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid.velocity = new_velocity_vector * 1.2

        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2.velocity =  new_velocity_vector2 * 1.2

#checking from VSS

