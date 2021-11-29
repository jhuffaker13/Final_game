import random
from game.point import Point
from game import constants

class RandomMovements:
    def __init__(self):
        pass

    def execute(self, cast):
        enemies = cast["enemies"]
        for enemy in enemies:
            random_move_number = random.randint(50, 100)
            random_direction = random.randint(1, 2000)
            if enemy.get_velocity().get_x() == 0 and enemy.get_velocity().get_y() == 0 :
                
                random_direction = random.randint(1,8)
                #print(random_direction)
            
            #enemy.set_velocity(Point(0,0))
            i = 0
            while i < random_move_number:
                if random_direction == 1:
                    enemy.set_velocity(Point(constants.ENEMY_PD, constants.ENEMY_Z))
                elif random_direction == 2:
                    enemy.set_velocity(Point(constants.ENEMY_ND, constants.ENEMY_Z))
                elif random_direction == 3:
                    enemy.set_velocity(Point(constants.ENEMY_Z, constants.ENEMY_PD))
                elif random_direction == 4:
                    enemy.set_velocity(Point(constants.ENEMY_Z, constants.ENEMY_ND))
                elif random_direction == 4:
                    enemy.set_velocity(Point(constants.ENEMY_Z, constants.ENEMY_ND))
                elif random_direction == 5:
                    enemy.set_velocity(Point(constants.ENEMY_PD, constants.ENEMY_ND))
                elif random_direction == 6:
                    enemy.set_velocity(Point(constants.ENEMY_ND, constants.ENEMY_ND))
                elif random_direction == 7:
                    enemy.set_velocity(Point(constants.ENEMY_PD, constants.ENEMY_PD))
                elif random_direction == 8:
                    enemy.set_velocity(Point(constants.ENEMY_ND, constants.ENEMY_PD))
                i += 1