from game import constants
from game.action import Action
#from game.weapon import Ball
from game.point import Point

class HandleOffScreenAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #laser = cast["balls"][0]
        lasers = cast["laser"]
        try:
            for group in cast.values():
                #for laser in lasers:
                for i in range(len(lasers)):
                    laser = cast["laser"][i]
                    if cast["laser"][i].get_position().get_x() > constants.MAX_X - 10:
                        lasers.remove(laser)
                        break
        except IndexError:
            pass
                    