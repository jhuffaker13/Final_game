import random
from game.point import Point

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
                    enemy.set_velocity(Point(3, 0))
                elif random_direction == 2:
                    enemy.set_velocity(Point(-3, 0))
                elif random_direction == 3:
                    enemy.set_velocity(Point(0, 3))
                elif random_direction == 4:
                    enemy.set_velocity(Point(0, -3))
                elif random_direction == 4:
                    enemy.set_velocity(Point(0, -3))
                elif random_direction == 5:
                    enemy.set_velocity(Point(3, -3))
                elif random_direction == 6:
                    enemy.set_velocity(Point(-3, -3))
                elif random_direction == 7:
                    enemy.set_velocity(Point(3, 3))
                elif random_direction == 8:
                    enemy.set_velocity(Point(-3, 3))
                i += 1