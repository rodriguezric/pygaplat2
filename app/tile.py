""" Module for Tile objects

Tiles represent colored squares or images that are painted
on the screen. They can have collision detection or not.
"""
from pygame.sprite import Sprite
from pygame import Surface

TILE_SIZE = 32

class ColorTile(Sprite):
    """ Base tile class

    Properties:
        pos (tuple(int, int)): The position of the Tile.
        color (str): The color of the Tile.
        image (Surface): The image for the Sprite class.
        rect (Rect): The rect for the Sprite class, used for positioning.
        surf (Surface): The Surface for the Sprite class.
    """
    def __init__(self, pos, color):
        """ Instantiates a ColorTile with color at pos

        Arguments:
            pos (tuple(int, int)): The position of the tile, topleft corner
            color (str): The color of the tile.
        """
        super().__init__()

        self.image = Surface((32, 32))
        self.surf = self.image
        self.rect = self.surf.get_rect(topleft=pos)

        self.surf.fill(color)
