import pygame
import random
import sounds

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Globals
crosshair_pos = [400, 300]
crosshair_speed = 5
crosshair_radius = 8

cast_location = None
cast_in_progress = False
fish_hooked = False
fish_caught = False

tension = 0
bite_timer = 0
bite_wait_time = 0
caught_timer = 0
score = 0

font = None

def set_font(f):
    global font
    font = f

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
    pygame.draw.rect(screen, WHITE, (50, 550, 200, 20), 2)
    bar_color = GREEN if tension < 60 else YELLOW if tension < 90 else RED
    pygame.draw.rect(screen, bar_color, (52, 552, tension * 1.96, 16))

def handle_input(event):
    global cast_in_progress, cast_location, fish_hooked
    global tension, bite_timer, bite_wait_time

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        if not cast_in_progress:
            cast_location = crosshair_pos.copy()
            cast_in_progress = True
            fish_hooked = False
            bite_timer = 0
            bite_wait_time = random.randint(60, 180)
            try:
                sounds.play_cast()
            except:
                pass
        elif fish_hooked:
            # Reel in
            global tension
            tension += 10
            if tension >= 100:
                try:
                    sounds.play_break()
                except:
                    pass
                reset_cast()

def update(screen, keys):
    global cast_in_progress, fish_hooked, fish_caught
    global tension, bite_timer, score, caught_timer

    # Move crosshair before casting
    if not cast_in_progress:
        if keys[pygame.K_LEFT]: crosshair_pos[0] -= crosshair_speed
        if keys[pygame.K_RIGHT]: crosshair_pos[0] += crosshair_speed
        if keys[pygame.K_UP]: crosshair_pos[1] -= crosshair_speed
        if keys[pygame.K_DOWN]: crosshair_pos[1] += crosshair_speed

    # Passive tension drop
    if cast_in_progress and fish_hooked:
        tension -= 1
        if tension <= 0:
            tension = 0
            fish_hooked = False
            cast_in_progress = False
            score += 1
            fish_caught = True
            caught_timer = 60
            try:
                sounds.play_catch()
            except:
                pass

    draw_crosshair(screen)

    if cast_in_progress:
        draw_cast_splash(screen)

        if not fish_hooked:
            bite_timer += 1
            if bite_timer >= bite_wait_time:
                fish_hooked = True
                tension = 30
                try:
                    sounds.play_bite()
                except:
                    pass

        if fish_hooked:
            screen.blit(font.render("Reel it in!", True, WHITE), (cast_location[0], cast_location[1] - 40))
            draw_tension_meter(screen)

    if fish_caught:
        caught_timer -= 1
        if caught_timer > 0:
            screen.blit(font.render("Fish Caught!", True, GREEN), (cast_location[0], cast_location[1] - 40))
        else:
            fish_caught = False

def reset_cast():
    global cast_in_progress, fish_hooked, tension
    cast_in_progress = False
    fish_hooked = False
    tension = 0

def get_score():
    return score

