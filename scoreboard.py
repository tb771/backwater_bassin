import pygame
import fishing_logic

font = None

def set_font(f):
    global font
    font = f

def draw_score(screen):
    score = fishing_logic.get_score()
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

