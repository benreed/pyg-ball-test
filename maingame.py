"""
Main module for prototype with remodeled
collision detection
Written Jan 11, 2016 by Benjamin Reed
	
Credit for this implementation goes to Sean J. McKiernan
(Mekire) at /r/pygame
https://github.com/Mekire
"""
import sys
import Queue

import pygame as pyg
import constants as con
from input import *
from objects import *
from stage import *

class App:
    """
    A class to cleanly encapsulate main game loop phases,
    including initialization, event handling, and state 
    updates
    """
    def __init__(self):
        """
        Get a reference to the display surface; set up required attributes;
        and instantiate player and stage objects
        """
        self.screen = pyg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pyg.time.Clock()
        self.fps = con.TARGET_FPS

        # Boolean members
        self.done = False
        
        # Key state variable
        self.keys = pyg.key.get_pressed()
      	
        # Initialize stage(s)
        self.stage_list = []
        self.stage_index = 0
        #self.test_stage = PlayStage(TESTSTAGE, self.player)
        self.test_stage = PlayStage(TESTSTAGE)
        self.stage_list.append(self.test_stage)
        self.current_stage = self.stage_list[self.stage_index]

        # Instantiate test objects and refer them to whatever
        #   stage needs to be "on point"
        self.ball = Ball(self.current_stage)
        self.ball2 = Ball(self.current_stage, 300, 70)
        self.current_stage.objects.append(self.ball)
        self.current_stage.objects.append(self.ball2)

    def event_loop(self):
        """
        Method encompassing one trip through the event queue
        Called within main_loop()
        """
        for event in pyg.event.get():
            # Poll for quit event
            if event.type == pyg.QUIT:
                self.done = True
            elif event.type in (pyg.KEYUP, pyg.KEYDOWN):
                # Update key state
                self.keys = pyg.key.get_pressed()

                # Put a corresponding InputEvent onto
                #   stage's input queue
                self.current_stage.input_queue.put(InputEvent(event.type, event.key))

    def render(self):
        """
        Draws to the screen and updates the display
        """
		
        # Draw level
        self.current_stage.draw(self.screen)
		
        # Draw game objects
        
        # Update display 
        pyg.display.flip()
		
    def main_loop(self):
        """
        Performs the main game loop
        """
        while not self.done:
            self.event_loop()
            # Update game objects
            self.current_stage.update()
            self.render()
            self.clock.tick(self.fps)
			
def main():
    """
    Main program function. Performs Pygame initialization,
    starts, and exits the program.
    """
    pyg.init()
    pyg.display.set_caption(con.WINDOW_CAPTION)
    pyg.display.set_mode(con.SCREEN_SIZE)
    App().main_loop()
    pyg.quit()
    sys.exit()
	
if __name__ == "__main__":
    main()
