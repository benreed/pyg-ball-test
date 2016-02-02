"""
Module for custom input classes and methods for
controllable characters
Written Dec 25, 2015 by Benjamin Reed
Version 0.0.1-alpha
"""
class InputEvent:
    """
    Class to encompass a Pygame input event
    (so as to retain type and key members)
    with a timestamp in frames since last input
    event recorded.
	
    (The intention is not just to timestamp,
    but also remember event type and event 
    key. That way the logical relationship
    between keyup/keydown for the same key
    is preserved even if the two events are
    separated in time by events for different
    keys.)
    """
    def __init__(self, type, key, timestamp):
        """
        Constructs an InputEvent with a Pygame
        event and a timestamp since previous
        event as members
        """
        self.type = type
        self.key = key
        self.timestamp = timestamp