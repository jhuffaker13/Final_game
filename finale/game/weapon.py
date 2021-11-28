from game.actor import Actor
from game import constants
from game.action import Action
from game.point import Point
from game.hero import Hero
import random


class Weapon():
    def __init__(self, input_service, hero_number):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        
        self._input_service = input_service
        self.hero_number = hero_number
        
        self.i = 0
        self.laserlist = []
        self.hero = Hero()

    def execute(self, cast):
        
        if self._input_service.is_space_pressed():
           
            
            
            laser = Actor()
            if cast["hero"][0].get_weapon() == 1:
                laser.set_image(constants.HERO_ONE)
                #print(self.hero.get_weapon())
            if cast["hero"][0].get_weapon() == 2:
                laser.set_image(constants.HERO_TWO)
            if cast["hero"][0].get_weapon() == 3:
                laser.set_image(constants.HERO_THREE)
            hero_x = cast["hero"][0].get_position().get_x()
            hero_y = cast["hero"][0].get_position().get_y()
            position = Point(hero_x + 10, hero_y)
            laser.set_height(constants.HERO_HEIGHT)
            laser.set_width(constants.HERO_WIDTH)
            laser.set_position(position)
            laser.set_velocity(Point(5, 0))
            self.laserlist.append(laser)
            cast["laser"] = self.laserlist
            #self.i += 1
        
            lasers = cast["laser"]
        
            for group in cast.values():
                #for laser in lasers:
                if len(lasers) > 5:
                    laser = cast["laser"][0]
                    
                    lasers.remove(laser)
                    break

        """enemies = cast["enemies"]
        for enemy in enemies:
            random_shot = random.randint(1, 1000)
            if random_shot == 1:
                laser = Actor()
                enemy_x = enemy.get_position().get_x()
                enemy_y = enemy.get_position().get_y()
                position = Point(enemy_x - 10, enemy_y)
                laser.set_image(constants.IMAGE_BALL)
                laser.set_height(constants.HERO_HEIGHT)
                laser.set_width(constants.HERO_WIDTH)
                laser.set_position(position)
                laser.set_velocity(Point(-5, 0))
                self.laserlist.append(laser)
                cast["enemyweapon"] = self.laserlist"""
