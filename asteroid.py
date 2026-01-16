import pygame, constants, circleshape, random
from logger import log_state, log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_rotation = random.uniform(20,50)
            new_angle_one = self.velocity.rotate(new_rotation)
            new_angle_two = self.velocity.rotate(-new_rotation)
            new_radius = self.radius-constants.ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = new_angle_one*1.2
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2.velocity = new_angle_two*1.2
