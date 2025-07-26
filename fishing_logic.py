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
tension = 0
bite_timer = 0
bite_wait_time = 0
reel_timer = 0
score = 0
cast_cooldown = 0  # 1.5 second cooldown (90 frames at 60 FPS)

font = None  # set from main

def set_font(f):
    global font
    font = f

def get_score():
    return score

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
    bar_color = GREEN if tension < 80 else YELLOW if tension < 100 else RED
    pygame.draw.rect(screen, bar_color, (52, 552, min(tension, 100) * 1.96, 16))

def handle_input(event):
    global cast_in_progress, cast_location, fish_hooked
    global tension, bite_timer, bite_wait_time, cast_cooldown

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and cast_cooldown == 0:
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
            tension += 10
            if tension >= 100:
                try:
                    sounds.play_break()
                except:
                    pass
                reset_cast()

def update(screen, keys):
    global cast_in_progress, fish_hooked, tension
    global bite_timer, reel_timer, score, cast_cooldown

    # Cooldown countdown
    if cast_cooldown > 0:
        cast_cooldown -= 1

    # Move crosshair
    if not cast_in_progress or cast_cooldown > 0:
        if keys[pygame.K_LEFT]: crosshair_pos[0] -= crosshair_speed
        if keys[pygame.K_RIGHT]: crosshair_pos[0] += crosshair_speed
        if keys[pygame.K_UP]: crosshair_pos[1] -= crosshair_speed
        if keys[pygame.K_DOWN]: crosshair_pos[1] += crosshair_speed

    draw_crosshair(screen)

    if cast_in_progress:
        draw_cast_splash(screen)

        if not fish_hooked:
            bite_timer += 1
            if bite_timer >= bite_wait_time:
                fish_hooked = True
                tension = 30
                reel_timer = 0
                try:
                    sounds.play_bite()
                except:
                    pass

        elif fish_hooked:
            # Tension decay
            tension = max(0, tension - 1)

            # Show reel warning
            screen.blit(font.render("Reel it in!", True, WHITE),
                        (cast_location[0], cast_location[1] - 40))
            draw_tension_meter(screen)

            # Catch logic
            if 20 < tension < 80:
                reel_timer += 1
                if reel_timer == 180:
                    try:
                        sounds.play_catch()
                    except:
                        pass
                    screen.blit(font.render("Fish Caught!", True, WHITE), (cast_location[0], cast_location[1] - 60))
                    score += 1
                    pygame.display.update()
                    pygame.time.delay(1000)
                    reset_cast()
            else:
                reel_timer = 0

            # Break or lose fish
            if tension >= 100:
                try:
                    sounds.play_break()
                except:
                    pass
                reset_cast()
            elif tension <= 0:
                reset_cast()

def reset_cast():
    global cast_in_progress, fish_hooked, tension, reel_timer, cast_cooldown
    cast_in_progress = False
    fish_hooked = False
    tension = 0
    reel_timer = 0
    cast_cooldown = 90  # 1.5 second delay

