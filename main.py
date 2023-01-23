import pygame
from sys import exit

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
fps = 60

def quit_game():
    pygame.quit()
    exit()

from app.tile import ColorTile

color_tile = ColorTile(pos=(32, 32),
                       color='red')

tile_group = pygame.sprite.Group()
tile_group.add(color_tile)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    tile_group.draw(screen)
    tile_group.update()

    pygame.display.update()
    clock.tick(fps)

quit_game()
