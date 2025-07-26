import pygame
from fishing_logic import cast_in_progress, crosshair_pos

def draw_fisherman(screen):
    base_x, base_y = 400, 550
    pole_tip = (base_x + 60, base_y - 100)
    pole_base = (base_x + 10, base_y - 30)

    # 🎣 Draw aiming line BEFORE fisherman, only if not cast yet
    if not cast_in_progress:
        pygame.draw.aaline(screen, (180, 180, 180), pole_tip, crosshair_pos)

    # 🧍 Draw fisherman
    pygame.draw.rect(screen, (160, 82, 45), (base_x - 20, base_y - 40, 40, 40))  # Overalls
    pygame.draw.circle(screen, (255, 224, 189), (base_x, base_y - 50), 10)       # Head
    pygame.draw.rect(screen, (100, 100, 100), (base_x - 25, base_y - 60, 50, 5)) # Hat brim
    pygame.draw.rect(screen, (120, 120, 120), (base_x - 15, base_y - 65, 30, 5)) # Hat top

    # 🪝 Fishing pole
    pygame.draw.line(screen, (80, 80, 80), pole_base, pole_tip, 2)

