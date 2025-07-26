import pygame
import random

# Fish appearance and movement
FISH_COLOR = (100, 200, 255)
FISH_SIZE = 12
FISH_SPEED_RANGE = (1, 2)
FISH_TURN_CHANCE = 0.02  # chance to randomly change direction

class Fish:
    def __init__(self, screen_width, screen_height):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.dx = random.choice([-1, 1]) * random.uniform(*FISH_SPEED_RANGE)
        self.dy = random.choice([-1, 1]) * random.uniform(*FISH_SPEED_RANGE)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        # Move fish
        self.x += self.dx
        self.y += self.dy

        # Bounce off edges
        if self.x < 0 or self.x > self.screen_width:
            self.dx *= -1
        if self.y < 0 or self.y > self.screen_height:
            self.dy *= -1

        # Occasionally turn randomly
        if random.random() < FISH_TURN_CHANCE:
            self.dx = random.choice([-1, 1]) * random.uniform(*FISH_SPEED_RANGE)
            self.dy = random.choice([-1, 1]) * random.uniform(*FISH_SPEED_RANGE)

    def draw(self, screen):
        pygame.draw.ellipse(screen, FISH_COLOR, (int(self.x), int(self.y), FISH_SIZE, FISH_SIZE // 2))


class FishSwarm:
    def __init__(self, count, screen_width, screen_height):
        self.fish_list = [Fish(screen_width, screen_height) for _ in range(count)]

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def draw(self, screen):
        for fish in self.fish_list:
            fish.draw(screen)

