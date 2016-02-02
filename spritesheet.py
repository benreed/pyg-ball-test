"""
Basic spritesheet module to handle slicing smaller images
from a larger one (minimize image loading for animation
frames)
Written Dec 20, 2015 by Benjamin Reed
Version 0.0.1-alpha
Credit for original implementation goes to
Paul Vincent Craven at
programarcadegames.com
"""
import pygame as pyg
import constants as con

class SpriteSheet(object):
    """
    Class used to contain a spritesheet image and 
    slice/manage individual images out of it
    """
    def __init__(self, filename):
        """
        Construct a SpriteSheet from image at file 
        path (filename) and convert pixel format
        """
        self.sprite_sheet = pyg.image.load(filename).convert()
        
    def get_image(self, x, y, width, height):
        """
        Grab a single image out of the sprite_sheet image
        Parameters: (x,y) for origin of the frame you wish
        to slice, and (width, height) for the dimensions of
        your desired slice
        """
        image = pyg.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
        
        # DEBUG: Transparency is color-keyed to a particular value
        #   (may change this later to alpha-based)
        image.set_colorkey(con.ALPHA_COLOR)
        
        return image