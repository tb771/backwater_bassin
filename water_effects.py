import pygame
import random
import math

RIPPLE_COLOR = (255, 255, 255, 40)  # translucent white

class Ripple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1
        self.max_radius = random.randint(20, 40)
        self.lifetime = 60
        self.age = 0

    def update(self):
        self.age += 1
        self.radius += 0.5

    def is_alive(self):
        return self.age < self.lifetime

    def draw(self, screen):
        alpha = max(0, 255 * (1 - self.age / self.lifetime))
        ripple_color = (*RIPPLE_COLOR[:3], int(alpha))
        ripple_surface = pygame.Surface((self.max_radius*2, self.max_radius*2), pygame.SRCALPHA)
        pygame.draw.circle(
            ripple_surface,
            ripple_color,
            (self.max_radius, self.max_radius),
            int(self.radius),
            1
        )
        screen.blit(ripple_surface, (self.x - self.max_radius, self.y - self.max_radius))


class WaterEffects:
    def __init__(self, screen_width, screen_height):
        self.ripples = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ripple_timer = 0

    def update(self):
        self.ripple_timer += 1
        if self.ripple_timer > random.randint(30, 90):
            self.spawn_random_ripple()
            self.ripple_timer = 0

        for ripple in self.ripples:
            ripple.update()

        self.ripples = [r for r in self.ripples if r.is_alive()]

    def spawn_random_ripple(self):
        x = random.randint(0, self.screen_width)
        y = random.randint(0, self.screen_height - 100)  # stay out of fisherman's zone
        self.ripples.append(Ripple(x, y))

    def draw(self, screen):
        for ripple in self.ripples:
            ripple.draw(screen)

