from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            random_velocity_1 = self.velocity.rotate(random_angle)
            random_velocity_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = random_velocity_1 * 1.2
            
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2.velocity = random_velocity_2 * 1.2

