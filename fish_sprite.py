import pygame

def load_fish_sprite():
    fish = pygame.Surface((32, 16), pygame.SRCALPHA)
    pygame.draw.ellipse(fish, (0, 200, 255), (4, 2, 24, 12))  # Body
    pygame.draw.polygon(fish, (0, 200, 255), [(0, 8), (6, 2), (6, 14)])  # Tail
    pygame.draw.circle(fish, (255, 255, 255), (24, 8), 3)  # Eye white
    pygame.draw.circle(fish, (0, 0, 0), (24, 8), 1)  # Eye pupil
    return fish

def draw_fish(screen, fish_img, location):
    screen.blit(fish_img, (location[0] - 16, location[1] - 8))

