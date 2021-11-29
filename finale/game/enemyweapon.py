from game.actor import Actor
from game import constants
from game.action import Action
from game.point import Point
from game.hero import Hero
import random

class EnemyWeapon():
    def __init__(self):
        self.enemylasers = []


    def execute(self, cast):
        enemies = cast["enemies"]
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
                self.enemylasers.append(laser)
                cast["enemyweapon"] = self.enemylasers