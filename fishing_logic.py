import pygame
import random

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

crosshair_pos = [400, 300]
crosshair_speed = 5
crosshair_radius = 8

cast_location = None
cast_in_progress = False
fish_hooked = False
tension = 0
bite_timer = 0
bite_wait_time = 0

font = pygame.font.SysFont(None, 36)

def draw_crosshair(screen):
    pygame.draw.circle(screen, WHITE, crosshair_pos, crosshair_radius, 2)
    pygame.draw.line(screen, WHITE, (crosshair_pos[0] - 10, crosshair_pos[1]),
                     (crosshair_pos[0] + 10, crosshair_pos[1]), 1)
    pygame.draw.line(screen, WHITE, (crosshair_pos[0], crosshair_pos[1] - 10),
                     (crosshair_pos[0], crosshair_pos[1] + 10), 1)

def draw_cast_splash(screen):
    if cast_location:
        pygame.draw.circle(screen, RED, cast_location, 10, 2)

def draw_tension_meter(screen):
    global tension
    pygame.draw.rect(screen, WHITE, (50, 550, 200, 20), 2)
    bar_color = GREEN if tension < 60 else YELLOW if tension < 90 else RED
    pygame.draw.rect(screen, bar_color, (52, 552, tension * 1.96, 16))

def handle_input(event):
    global cast_in_progress, cast_location, fish_hooked
    global tension, bite_timer, bite_wait_time

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if not cast_in_progress:
                cast_location = crosshair_pos.copy()
                cast_in_progress = True
                fish_hooked = False
                bite_timer = 0
                bite_wait_time = random.randint(60, 180)
            elif fish_hooked:
                tension += 10
                if tension >= 100:
                    cast_in_progress = False
                    fish_hooked = False
                    tension = 0

def update(screen, keys):
    global cast_in_progress, fish_hooked, tension, bite_timer

    if not cast_in_progress:
        if keys[pygame.K_LEFT]: crosshair_pos[0] -= crosshair_speed
        if keys[pygame.K_RIGHT]: crosshair_pos[0] += crosshair_speed
        if keys[pygame.K_UP]: crosshair_pos[1] -= crosshair_speed
        if keys[pygame.K_DOWN]: crosshair_pos[1] += crosshair_speed
    elif fish_hooked:
        tension -= 1
        if tension <= 0:
            cast_in_progress = False
            fish_hooked = False
            tension = 0
            screen.blit(font.render("Fish caught!", True, GREEN), (cast_location[0], cast_location[1] - 40))

    draw_crosshair(screen)
    if cast_in_progress:
        draw_cast_splash(screen)
        if not fish_hooked:
            bite_timer += 1
            if bite_timer >= bite_wait_time:
                fish_hooked = True
                tension = 30
        if fish_hooked:
            screen.blit(font.render("Reel it in!", True, WHITE), (cast_location[0], cast_location[1] - 40))
            draw_tension_meter(screen)
