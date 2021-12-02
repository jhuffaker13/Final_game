import raylibpy
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.actor import Actor
from game import constants
from game.input_service import InputService
import random

class Enemy(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(constants.HERO_WIDTH)
        self.set_height(constants.HERO_HEIGHT)
        self.set_image(constants.ENEMY)
        self.set_velocity(Point(constants.ENEMY_ND, constants.ENEMY_Z))
        self.weapon = 1
        self.health = 100
        self.input_service = InputService
        

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health
    
    
            


    

    