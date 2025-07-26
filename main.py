import pygame
import sys
import fishing_logic as fish
import fish_sprite
import fisherman
import scoreboard
from fish_swarm import FishSwarm


# Init
pygame.init()

swarm = FishSwarm(count=10, screen_width=800, screen_height=600)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Backwater Bassin'")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
fish.set_font(font)
scoreboard.set_font(font)

fish_img = fish_sprite.load_fish_sprite()

def main():
    running = True
    while running:
        screen.fill((70, 130, 180))  # water color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            fish.handle_input(event)

        keys = pygame.key.get_pressed()
        fish.update(screen, keys)

        if fish.fish_hooked:
            fish_sprite.draw_fish(screen, fish_img, fish.cast_location)

        fisherman.draw_fisherman(screen)
        scoreboard.draw_score(screen)
#random fish activity
        swarm.update()
        swarm.draw(screen)
  

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

