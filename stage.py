"""
Module for game "stages", including both
stages where gameplay takes place and 
configuration screens
Also includes basic stage objects such as 
surfaces
Written Jan 11, 2016 by Benjamin Reed
Version 0.0.1-alpha

Credit for original implementation goes to
Paul Vincent Craven at 
programarcadegames.com
"""

import pygame as pyg
import constants as con
from objects import *

"""
Stage constants defined up here
"""
# Simplifying concept for now -- working only with a box
#   made of lines to delineate stage boundaries
TESTSTAGE = {
    "FLOOR"      : con.SCREEN_HEIGHT-15,
    "CEILING"    : 15,
    "LEFT_WALL"  : 15,
    "RIGHT_WALL" : con.SCREEN_WIDTH-15,
    "GRAVITY"    : 0.35
}

class Stage(object):
    """
    Generic stage superclass. Has basic functionality
    to wipe and update display contents.
    """
    def __init__(self):
        """
        Initializes background to a window-sized surface
        colored with the background color
        """
        self.background = pyg.Surface([con.SCREEN_WIDTH, con.SCREEN_HEIGHT])
        self.background.fill(con.BG_COLOR)
        
    def draw(self, screen):
        """
        Blits the background color to display surface
        to wipe previous frame's contents
        """
        screen.blit(self.background,[0,0])
        
class PlayStage(Stage):
    """
    A Stage meant to manage gameplay objects, including 
    player characters, background objects, etc.
    """
    def __init__(self, stage):
        """
        Calls superconstructor and defines floor,
        ceiling, and wall values
        """
        super(PlayStage, self).__init__()

        # Stage boundary values
        self.floor = stage["FLOOR"]
        self.ceiling = stage["CEILING"]
        self.left_wall = stage["LEFT_WALL"]
        self.right_wall = stage["RIGHT_WALL"]

        # Universal stage gravity
        self.gravity = stage["GRAVITY"]

        # Instantiate test objects here
        self.objects = []

    def update(self):
        """
        Update stage state. Responsible for updating
        some state properties of object members (which
        ones and to what extent may change in later 
        versions)
        """
        if self.objects:
            # Apply gravity to all gravity-subject game
            #   objects in stage
            self.apply_gravity()

            # Update game object states
            for object in self.objects:
                object.update()
            
    def draw(self, screen):
        """
        Wipes previous frame's contents with 
        background and draws game surface members
        """
        # Blit background 
        screen.blit(self.background,[0,0])
        
        # Draw primitive lines to delineate ceiling,
        #   floor, and walls
        pyg.draw.line(screen, con.GREEN, (0, self.floor), (con.SCREEN_WIDTH, self.floor))
        pyg.draw.line(screen, con.GREEN, (0, self.ceiling), (con.SCREEN_WIDTH, self.ceiling))
        pyg.draw.line(screen, con.GREEN, (self.left_wall, 0), (self.left_wall, con.SCREEN_HEIGHT))
        pyg.draw.line(screen, con.GREEN, (self.right_wall, 0), (self.right_wall, con.SCREEN_HEIGHT))

        # Draw game objects (if there are any)
        if self.objects:
            for object in self.objects:
                object.draw(screen)

    def apply_gravity(self):
        """
        Applies stage gravity to all gravity-subject game 
        objects within the stage
        """
        for object in self.objects:
            if isinstance(object, GravityObject) and object.is_gravity:
                if not object.deltaY == 0:
                    object.deltaY += self.gravity
