import pygame as pyg
import constants as con

class TypedRect(pyg.Rect):
    """
    An extended Pygame rect with a type flag
    indicating what type of collision detection
    it is used for
    Used for basic, non-rotated AABB collision 
    """
    def __init__(self, type, x, y, width, height):
        """
        Calls Pygame rect superconstructor and adds an
        associated type value
        """
        super(TypedRect, self).__init__(x, y, width, height)
        self.type = type

class MovableObject(pyg.sprite.Sprite):
    """
    Generic Sprite object with a deltaX & a deltaY
    property
    """
    def __init__(self, stage, x=50, y=50):
        super(MovableObject, self).__init__()

        # Pygame clock to time events
        self.clock = pyg.time.Clock()

        # Basic 2D speed dimensions
        self.deltaX = 5
        self.deltaY = 0

        # Rectangle defining spatial coordinates
        #   of pushbox
        self.rect = TypedRect("Sprite", x, y, 30, 50)

        # Red surface as placeholder image
        self.image = pyg.Surface((30, 50))
        self.image.fill(con.RED)

        # Define the drawing rect
        self.draw_rect = self.image.get_rect()
        self.draw_rect.x = x
        self.draw_rect.y = y

        # Pushbox defines limits of sprite penetration
        # NOT logically identical to the drawing rect
        self.pushbox = self.image.get_rect()
        self.pushbox.x = self.draw_rect.x
        self.pushbox.y = self.draw_rect.y

        # Reference to whatever stage the object
        #   inhabits (initially None)
        self.stage = stage

    def update(self):
        """
        Updates the object's game state
        """
        # Move along x-axis
        self.move_x()

        # Move along y-axis
        self.move_y()
 
        # Tick the clock
        self.clock.tick()

    def draw(self, screen):
        """
        Draws the object's sprite to the screen
        """
        # Blit sprite
        screen.blit(self.image, self.draw_rect)
        # If in debug mode, draw collision rects
        if con.DEBUG:
            pyg.draw.rect(screen, con.WHITE, self.draw_rect, 1)
            pyg.draw.rect(screen, con.GREEN, self.pushbox, 1)

    def move_x(self):
        """
        Moves object along the x axis by delta
        value
        """
        self.draw_rect.x += self.deltaX
        self.pushbox.x += self.deltaX

    def move_y(self):
        """
        Moves object along the y axis by delta
        value
        """
        self.draw_rect.y += self.deltaY
        self.pushbox.y += self.deltaY

    def stop_bound(self):
        """
        Stops movement & adjusts position
        when object collides with stage 
        boundaries (ceiling, walls, floor)
        """

class GravityObject(MovableObject):
    """
    Game object subject to gravity
    """
    def __init__(self, stage):
        """
        Calls superconstructor and initializes 
        gravity modifier
        """
        super(GravityObject, self).__init__(stage)

        # Object-specific gravity modifier
        #   (modifies the base influence of stage
        #   gravity)
        self.grav_modifier = 0

class FrictionObject(GravityObject):
    """
    Game object subject to friction (decay of deltaX)
    Currently extends GravityObject, but I may change
       this later to only implement friction
    """
    def __init__(self, stage):
        """
        Calls superconstructor and initializes friction
        value
        """
        super(FrictionObject, self).__init__(stage)
        self.friction = 0.35

    def apply_friction(self):
        """
        Applies friction to deltaX
        """
        self.deltaX += self.friction


class Ball(FrictionObject):
    """
    A bouncy ball that is subject to gravity.
    Meant to mimick a soft round ball like a
    basketball or volleyball, with light 
    weight and high elasticity (faked for
    simplicity of design)
    """
    def __init__(self, stage, x=50, y=50):
        """
        Loads ball image and sets rect to sprite
        rect
        """
        super(Ball, self).__init__(stage)

        # Redefine image member & drawing rect
        self.image = pyg.image.load("img/ball.png").convert_alpha()
        self.draw_rect = self.image.get_rect()
        self.draw_rect.x = x
        self.draw_rect.y = y

        # Redefine pushbox
        self.pushbox = self.image.get_rect()
        self.pushbox.x = self.draw_rect.x
        self.pushbox.y = self.draw_rect.y

        # Set state flags & such
        self.can_bounce = True

    def update(self):
        """
        Moves ball and bounces it if it hits a
        stage boundary
        """
        # Move along x-axis
        self.move_x()

        # Check for collision (x-axis)
        self.check_col_x()

        # Move along y-axis
        self.move_y()

        # Check for collision (y-axis)
        self.check_col_y()

        # Tick the clock for event timekeeping
        self.clock.tick()

    def bounce(self):
        """
        Bounces ball when it collides with a stage 
        boundary (ceiling, wall, floor)
        Checks timer to ensure ball cannot bounce
        too rapidly (thus creating "micro-bounces"
        if the ball will not clear the ground by
        the next frame)
        """
        # Set deltaY equal to a proportion of inverse
        print "deltaY pre-bounce  : " + str(self.deltaY)
        self.deltaY = -0.75*self.deltaY

    def check_col_x(self):
        """
        Checks for collisions along x-axis
        """
        # Left wall collision
        if self.pushbox.left < self.stage.left_wall:
            # Set left edge to wall
            self.draw_rect.left = self.stage.left_wall
            self.pushbox.left = self.stage.left_wall
            
            # Invert deltaX
            self.deltaX = -self.deltaX

        # Right wall collision
        elif self.pushbox.right > self.stage.right_wall:
            # Set right edge to wall
            self.draw_rect.right = self.stage.right_wall
            self.pushbox.right = self.stage.right_wall

            # Invert deltaX
            self.deltaX = -self.deltaX

    def check_col_y(self):
        """
        Checks for collisions along y-axis
        """        
        # Floor collision
        if self.pushbox.bottom > self.stage.floor:
            # Forcibly re-align pushbox & drawing rect
            #   to floor to prevent being at or below 
            #   floor for more than 1 frame
            self.draw_rect.bottom = self.stage.floor
            self.pushbox.bottom = self.stage.floor

            # Bounce off the floor
            if self.can_bounce:
                self.bounce()
            else:
                self.deltaY = 0
                self.apply_friction()

        # Ceiling collision
        elif self.pushbox.top < self.stage.ceiling:
            # Adjust rects
            self.draw_rect.top = self.stage.ceiling
            self.pushbox.top = self.stage.ceiling

            # Invert deltaY
            self.deltaY = -self.deltaY
