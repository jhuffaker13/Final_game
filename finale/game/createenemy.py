from game.action import Action
from game.enemy import Enemy
from game.point import Point
from game import constants
import random

class CreateEnemy(Action):
    def __init__(self):
        self._enemycount = 22

    def execute(self, cast):
        for group in cast.values():
            enemies = cast["enemies"]
            if self._enemycount != 0:
                 while len(enemies) < 8 and self._enemycount != 0:
                    enemy = Enemy()
                    random_y = random.randint(100, constants.MAX_Y - 100)
                    position = Point(1300, random_y)
                    enemy.set_position(position)
                    enemy.set_velocity(Point(constants.ENEMY_ND, constants.ENEMY_Z))
                    enemies.append(enemy)
                    cast["enemies"] = enemies
                        
                    self._enemycount -= 1

            elif self._enemycount == 0 and len(enemies) == 0:
                print("Win!")
