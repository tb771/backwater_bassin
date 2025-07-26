import pygame
import random

def draw_grass(screen, screen_width, screen_height):
    ground_y = screen_height - 10
    for x in range(0, screen_width, 6):
        blade_height = random.randint(8, 14)
        color = (34, 139, 34)  # Forest green
        pygame.draw.line(screen, color, (x, ground_y), (x, ground_y - blade_height), 1)

