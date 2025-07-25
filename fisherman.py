import pygame

def draw_fisherman(screen):
    # Simple figure in suspenders and hat
    base_x, base_y = 400, 550
    pygame.draw.rect(screen, (160, 82, 45), (base_x - 20, base_y - 40, 40, 40))  # Overalls
    pygame.draw.circle(screen, (255, 224, 189), (base_x, base_y - 50), 10)  # Head
    pygame.draw.rect(screen, (100, 100, 100), (base_x - 25, base_y - 60, 50, 5))  # Hat brim
    pygame.draw.rect(screen, (120, 120, 120), (base_x - 15, base_y - 65, 30, 5))  # Hat top

