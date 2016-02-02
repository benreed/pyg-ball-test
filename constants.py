"""
Constant values of application scope
Written Jan 2, 2016 by Benjamin Reed
Version 0.0.1-alpha
"""

"""
Game constants
"""
# Global flag used to toggle debugging functions
#   such as drawing collision rects, FPS,
#   etc
DEBUG = True

# Game version
GAME_VERSION = "0.0.1-alpha"

# Target frame rate
TARGET_FPS = 60

# Primitive colors
BLACK    =    (   0,   0,   0)
BLUE     =    (   0,   0, 255)
CYAN     =    (   0, 255, 255)
GREEN    =    (   0, 255,   0)
PURPLE   =    ( 255,   0, 255)
RED      =    ( 255,   0,   0)
WHITE    =    ( 255, 255, 255)
YELLOW   =    ( 255, 255,   0)

BG_COLOR =    (   0, 155, 200)
ALPHA_COLOR = ( 255,   0, 192)

# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Game window caption
WINDOW_CAPTION = "Prototype " + GAME_VERSION

"""
Character constants
"""

"""
Tuple member legend:
   [0]     : Pseudo-key naming frame (used to make a real key)
   [1]     : Drawing axis : Delineates what space is considered
             "in front of" or "behind" the character when facing
			 left or right
   [2]     : Sprite collision rect : Used to determine collision 
             with surfaces and other sprites, e.g.:
		     * Keeps sprites from clipping thru walls, ceiling, floor
		     * Determines how deep sprites can clip into each other
		     * In advanced hit states, may determine if character hits 
		     a surface and is subject to a splat, knockdown, etc
			 (this day is yet far off...)
   [3...n] : Vulnerability and attack collision rects : Of indeterminate 
             number. Most frames have at least 1 "Vuln" rect, 
			 but only specific frames will have 1 or more "Atk" rects.
"""

PHO_ANIM = (
	( "IDLE_1",   40, ("Sprite", 30, 46, 25, 68), ("Vuln", 32, 50, 22, 64), ("Vuln", 34, 30, 16, 20) ),
	( "CROUCH_1", 40, ("Sprite", 39, 66, 20, 48), ("Vuln", 40, 68, 20, 20), ("Vuln", 32, 88, 28, 26), ("Vuln", 44, 52, 13, 16) ),
	( "RUN_1",    40, ("Sprite", 50, 50, 25, 64), ("Vuln", 52, 54, 22, 60), ("Vuln", 72, 47, 16, 14) ),
	( "RUN_2",    40, ("Sprite", 55, 50, 25, 64), ("Vuln", 57, 54, 22, 60), ("Vuln", 67, 42, 16, 14) ),
	( "RUN_3",    40, ("Sprite", 42, 50, 25, 64), ("Vuln", 47, 54, 19, 60), ("Vuln", 54, 37, 13, 17) ),
	( "RUN_4",    40, ("Sprite", 50, 50, 25, 64), ("Vuln", 52, 54, 22, 60), ("Vuln", 72, 47, 16, 14) ),
	( "RUN_5",    40, ("Sprite", 55, 50, 25, 64), ("Vuln", 52, 54, 22, 60), ("Vuln", 67, 42, 16, 14) ),
	( "RUN_6",    40, ("Sprite", 42, 50, 25, 64), ("Vuln", 47, 54, 19, 60), ("Vuln", 54, 37, 13, 17) ),
	( "JUMP_1",   40, ("Sprite", 56, 45, 25, 45), ("Vuln", 58, 48, 19, 39), ("Vuln", 72, 37, 16, 14) ),
	( "JUMP_2",   40, ("Sprite", 56, 55, 25, 45), ("Vuln", 58, 58, 19, 39), ("Vuln", 72, 47, 16, 14) ),
	( "JUMP_3",   40, ("Sprite", 56, 45, 25, 45), ("Vuln", 58, 48, 19, 39), ("Vuln", 72, 35, 16, 14) ),
	( "JUMP_4",   40, ("Sprite", 46, 45, 25, 45), ("Vuln", 48, 48, 19, 39), ("Vuln", 64, 37, 16, 14))
)

PHOEBE = {
	"NAME"            : "Phoebe",
	"SPRITESHEET"     : "img/nov2015_spritesheet_2.png",
	"ANIMS"           : PHO_ANIM,
	"IMAGE_WIDTH"     : 120,
	"IMAGE_HEIGHT"    : 114,
	"NUM_OF_FRAMES"   : 12,
	
	"RUN_SPEED"       : 6,
	"AIR_STEER_SPEED" : 3,
	"JUMP_FORCE"      : -10,
	"GRAVITY"         : 0.45
}