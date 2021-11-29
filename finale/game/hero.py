import raylibpy
from game.change_color import ChangeColor
from game.control_actors_action import ControlActorsAction
from game.actor import Actor
from game import constants
from game.input_service import InputService

class Hero(Actor):
    def __init__(self):
        super().__init__()
        self.change_color = ChangeColor
        self.set_width(constants.HERO_WIDTH)
        self.set_height(constants.HERO_HEIGHT)
        self.set_image(constants.HERO_TWO)
        self.weapon = 1
        self.input_service = InputService
        self.health = 100
        
    

    def change_hero_color(self):
        self.change_color.execute()
        #print(self.weapon)

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health
    

    

    