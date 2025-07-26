import pygame
from fishing_logic import cast_location, cast_in_progress

def draw_fisherman(screen):
    base_x, base_y = 400, 550

    # Body (overalls)
    pygame.draw.rect(screen, (160, 82, 45), (base_x - 20, base_y - 40, 40, 40))

    # Head
    pygame.draw.circle(screen, (255, 224, 189), (base_x, base_y - 50), 10)

    # Hat
    pygame.draw.rect(screen, (100, 100, 100), (base_x - 25, base_y - 60, 50, 5))  # Brim
    pygame.draw.rect(screen, (120, 120, 120), (base_x - 15, base_y - 65, 30, 5))  # Top

    # 🎣 Fishing pole
    pole_base = (base_x + 10, base_y - 30)
    pole_tip = (base_x + 60, base_y - 100)
    pygame.draw.line(screen, (80, 80, 80), pole_base, pole_tip, 2)

    # 🧵 Fishing line (cast line to splash)
    if cast_in_progress and cast_location:
        pygame.draw.aaline(screen, (200, 200, 200), pole_tip, cast_location)

