import sys
import pygame


def run_game():
    pygame.display.set_caption("Alien Invasion")


pygame.init()

bg_color = (230, 230, 230)
screen = pygame.display.set_mode((1200, 800))

run_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(bg_color)
    pygame.display.flip()


