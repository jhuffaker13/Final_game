from game import constants
from game.action import Action
#from game.weapon import Ball
from game.point import Point
import random

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
        enemies = cast["enemies"]
        try:
            for group in cast.values():
                #for laser in lasers:
                for i in range(len(lasers)):
                    laser = cast["laser"][i]
                    if cast["laser"][i].get_position().get_x() > constants.MAX_X - 10:
                        lasers.remove(laser)
                        break
                for enemy in enemies:
                    if enemy.get_position().get_y() > constants.MAX_Y - 50:
                        change_direction = random.randint(1,3)
                        if change_direction == 1:
                            enemy.set_velocity(Point(-3, -3))
                        elif change_direction == 2:
                            enemy.set_velocity(Point(3, -3))
                        elif change_direction == 3:
                            enemy.set_velocity(Point(0, -3))

                    if enemy.get_position().get_y() < (50 + constants.MAX_Y) - constants.MAX_Y:
                        change_direction = random.randint(1,3)
                        if change_direction == 1:
                            enemy.set_velocity(Point(-3, 3))
                        elif change_direction == 2:
                            enemy.set_velocity(Point(3, 3))
                        elif change_direction == 3:
                            enemy.set_velocity(Point(0, 3))

                    if enemy.get_position().get_x() > constants.MAX_X - 50:
                        change_direction = random.randint(1,3)
                        if change_direction == 1:
                            enemy.set_velocity(Point(-3, 0))
                        elif change_direction == 2:
                            enemy.set_velocity(Point(-3, 3))
                        elif change_direction == 3:
                            enemy.set_velocity(Point(-3, -3))
                        
                    if enemy.get_position().get_x() < constants.MAX_X - 800:
                        change_direction = random.randint(1,3)
                        if change_direction == 1:
                            enemy.set_velocity(Point(3, 0))
                        elif change_direction == 2:
                            enemy.set_velocity(Point(3, 3))
                        elif change_direction == 3:
                            enemy.set_velocity(Point(3, -3))
                        
                       
        except IndexError:
            pass
                    