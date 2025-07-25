import pygame

score = 0
font = None

def set_font(f):
    global font
    font = f


def increment_score():
    global score
    score += 1

def draw_score(screen):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (650, 20))

