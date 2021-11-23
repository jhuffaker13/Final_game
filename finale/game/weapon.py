from game.actor import Actor
from game import constants
from game.action import Action
from game.point import Point


class Weapon():
    def __init__(self, input_service, hero_number):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self.hero_number = hero_number

    def execute(self, cast):
        i = 1
        if self._input_service.is_space_pressed():
            print("It worked")
            
            laserlist = []
            laser = Actor()
            laser.set_image(constants.HERO_ONE)
            position = Point(600, 300)
            laser.set_position(position)
            laser.set_velocity(Point(constants.HERO_DX, constants.HERO_DY))
            laserlist.append(laser)
            cast["laser"] = laserlist
            i += 1


            #return cast