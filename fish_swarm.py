import pygame
import random
import math

# Fish appearance
FISH_COLOR = (218, 165, 32)  # Golden-orange
FISH_TURN_CHANCE = 0.02
IDLE_CHANCE = 0.01
TAIL_WAG_SPEED = 0.15  # radians per frame

class Fish:
    def __init__(self, screen_width, screen_height):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.size = random.choice([10, 14, 18])  # small, medium, large

        base_speed = max(0.4, 10 / self.size)
        self.dx = random.choice([-1, 1]) * random.uniform(base_speed * 0.5, base_speed)
        self.dy = random.choice([-1, 1]) * random.uniform(base_speed * 0.5, base_speed)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.tail_phase = random.uniform(0, 2 * math.pi)  # tail animation offset
        self.idle_frames = 0

    def update(self):
        # If idling, decrement idle time and skip movement
        if self.idle_frames > 0:
            self.idle_frames -= 1
            return

        self.x += self.dx
        self.y += self.dy

        if self.x < 0 or self.x > self.screen_width:
            self.dx *= -1
        if self.y < 0 or self.y > self.screen_height:
            self.dy *= -1

        if random.random() < FISH_TURN_CHANCE:
            base_speed = max(0.4, 10 / self.size)
            self.dx = random.choice([-1, 1]) * random.uniform(base_speed * 0.5, base_speed)
            self.dy = random.choice([-1, 1]) * random.uniform(base_speed * 0.5, base_speed)

        if random.random() < IDLE_CHANCE:
            self.idle_frames = random.randint(60, 120)  # idle 1–2 seconds

        self.tail_phase += TAIL_WAG_SPEED

    def draw(self, screen):
        body_width = self.size
        body_height = self.size // 2
        body_rect = pygame.Rect(int(self.x), int(self.y), body_width, body_height)
        pygame.draw.ellipse(screen, FISH_COLOR, body_rect)

        # Tail flick — small triangle that oscillates
        tail_length = body_width // 2
        tail_angle = math.sin(self.tail_phase) * 5  # oscillate ±5 degrees

        tail_center_x = self.x
        tail_center_y = self.y + body_height // 2

        tail_points = [
            (tail_center_x, tail_center_y),
            (
                tail_center_x - tail_length,
                tail_center_y - tail_length // 2
            ),
            (
                tail_center_x - tail_length,
                tail_center_y + tail_length // 2
            )
        ]

        rotated_tail = []
        for px, py in tail_points:
            dx = px - tail_center_x
            dy = py - tail_center_y
            angle = math.radians(tail_angle)
            rx = dx * math.cos(angle) - dy * math.sin(angle)
            ry = dx * math.sin(angle) + dy * math.cos(angle)
            rotated_tail.append((tail_center_x + rx, tail_center_y + ry))

        pygame.draw.polygon(screen, FISH_COLOR, rotated_tail)

class FishSwarm:
    def __init__(self, count, screen_width, screen_height):
        self.fish_list = [Fish(screen_width, screen_height) for _ in range(count)]

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def draw(self, screen):
        for fish in self.fish_list:
            fish.draw(screen)

