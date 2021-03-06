from game.actor import Actor
from game import constants
from game.point import Point
from game.action import Action

class HeroWeapon():    
    def __init__(self, input_service):
        self._input_service = input_service
        self.laserlist = []
        self.charge = 0
        #self.distance = constants.MAX_X
    
    def execute(self, cast):
        if cast["hero"][0].get_weapon() == 1:
            
            if self._input_service.is_space_held():
                self.charge += 1

            if self._input_service.is_space_released():
                if cast["hero"][0].get_weapon() == 1:
                    laser = Actor()
                    hero_x = cast["hero"][0].get_position().get_x()
                    hero_y = cast["hero"][0].get_position().get_y()
                    if self.charge < 50:
                        damage = 25
                        laser.set_image(constants.HERO_ONE_LASER)
                        position = Point(hero_x + 10, hero_y + 32)
                    elif self.charge > 50 and self.charge < 100:
                        damage = 40
                        laser.set_image(constants.HERO_ONE_MEDIUM_LASER)
                        position = Point(hero_x + 10, hero_y + 29)
                    elif self.charge > 100:
                        damage = 60
                        laser.set_image(constants.HERO_ONE_LARGE_LASER)
                        position = Point(hero_x + 10, hero_y + 23)
                    
                    
                    laser.set_damage(damage)
                    
                    
                    laser.set_height(constants.LASER_HEIGHT)
                    laser.set_width(constants.LASER_WIDTH)
                    laser.set_position(position)
                    laser.set_velocity(Point(constants.HERO_LASER, 0))
                    self.laserlist.append(laser)
                    cast["laser"] = self.laserlist
                    #print(f"This is x {self.charge}")
                    self.charge = 0

        elif cast["hero"][0].get_weapon() == 2 or cast["hero"][0].get_weapon() == 3:
            

            if self._input_service.is_space_pressed():
            
                
                
                """laser = Actor()
                if cast["hero"][0].get_weapon() == 1:
                    laser.set_image(constants.HERO_ONE)
                    #print(self.hero.get_weapon())
                    laser.set_damage(25)
                if cast["hero"][0].get_weapon() == 2:
                    laser.set_image(constants.HERO_TWO)
                    laser.set_damage(20)
                if cast["hero"][0].get_weapon() == 3:
                    laser.set_image(constants.HERO_THREE)
                    laser.set_damage(50)
                hero_x = cast["hero"][0].get_position().get_x()
                hero_y = cast["hero"][0].get_position().get_y()
                position = Point(hero_x + 10, hero_y)
                laser.set_height(constants.HERO_HEIGHT)
                laser.set_width(constants.HERO_WIDTH)
                laser.set_position(position)
                laser.set_velocity(Point(constants.HERO_LASER, 0))
                self.laserlist.append(laser)
                cast["laser"] = self.laserlist
                #self.i += 1"""

                """if cast["hero"][0].get_weapon() == 1:
                    laser = Actor()
                    laser.set_image(constants.HERO_ONE_LASER)
                    laser.set_damage(35)
                    hero_x = cast["hero"][0].get_position().get_x()
                    hero_y = cast["hero"][0].get_position().get_y()
                    position = Point(hero_x + 10, hero_y + 32)
                    laser.set_height(constants.LASER_HEIGHT)
                    laser.set_width(constants.LASER_WIDTH)
                    laser.set_position(position)
                    laser.set_velocity(Point(constants.HERO_LASER, 0))
                    self.laserlist.append(laser)
                    cast["laser"] = self.laserlist"""

                if cast["hero"][0].get_weapon() == 2:
                    laser = Actor()
                    laser.set_image(constants.HERO_TWO_LASER)
                    laser.set_damage(35)
                    hero_x = cast["hero"][0].get_position().get_x()
                    hero_y = cast["hero"][0].get_position().get_y()
                    position = Point(hero_x + 10, hero_y + 20)
                    laser.set_height(constants.LASER_HEIGHT)
                    laser.set_width(constants.LASER_WIDTH)
                    laser.set_position(position)
                    laser.set_velocity(Point(constants.HERO_LASER, 0))
                    laser.set_distance(hero_x + constants.YELLOW_MAX)
                    self.laserlist.append(laser)
                    cast["laser"] = self.laserlist
                    #Second laser starts here
                    laser = Actor()
                    laser.set_image(constants.HERO_TWO_LASER)
                    laser.set_damage(35)
                    hero_x = cast["hero"][0].get_position().get_x()
                    hero_y = cast["hero"][0].get_position().get_y()
                    position = Point(hero_x + 10, hero_y + 44)
                    laser.set_height(constants.LASER_HEIGHT)
                    laser.set_width(constants.LASER_WIDTH)
                    laser.set_position(position)
                    laser.set_velocity(Point(constants.HERO_LASER, 0))
                    laser.set_distance(hero_x + constants.YELLOW_MAX)
                    self.laserlist.append(laser)
                    cast["laser"] = self.laserlist

                if cast["hero"][0].get_weapon() == 3:
                    laser = Actor()
                    laser.set_image(constants.HERO_THREE_LASER)
                    laser.set_damage(15)
                    hero_x = cast["hero"][0].get_position().get_x()
                    hero_y = cast["hero"][0].get_position().get_y()
                    position = Point(hero_x + 10, hero_y + 32)
                    laser.set_height(constants.LASER_HEIGHT)
                    laser.set_width(constants.LASER_WIDTH)
                    laser.set_position(position)
                    laser.set_velocity(Point(constants.HERO_LASER, 0))
                    self.laserlist.append(laser)
                    cast["laser"] = self.laserlist
                    #First diagonal laser starts here
                    laser = Actor()
                    laser.set_image(constants.HERO_THREE_DOWN_LASER)
                    laser.set_damage(25)
                    hero_x = cast["hero"][0].get_position().get_x()
                    hero_y = cast["hero"][0].get_position().get_y()
                    position = Point(hero_x + 10, hero_y + 34)
                    laser.set_height(constants.LASER_HEIGHT)
                    laser.set_width(constants.LASER_WIDTH)
                    laser.set_position(position)
                    laser.set_velocity(Point(constants.HERO_LASER, constants.HERO_LASER/5))
                    self.laserlist.append(laser)
                    cast["laser"] = self.laserlist
                    #Second diagonal laser starts here
                    laser = Actor()
                    laser.set_image(constants.HERO_THREE_UP_LASER)
                    laser.set_damage(25)
                    hero_x = cast["hero"][0].get_position().get_x()
                    hero_y = cast["hero"][0].get_position().get_y()
                    position = Point(hero_x + 10, hero_y - 10)
                    laser.set_height(constants.LASER_HEIGHT)
                    laser.set_width(constants.LASER_WIDTH)
                    laser.set_position(position)
                    laser.set_velocity(Point(constants.HERO_LASER, constants.HERO_LASER * -1/5))
                    self.laserlist.append(laser)
                    cast["laser"] = self.laserlist

                lasers = cast["laser"]
            

                #Placed this cose elsewhere, was not working while in this area. Leaving it here just in case
                """for group in cast.values():
                    #for laser in lasers:
                    while len(lasers) > 6:
                        laser = cast["laser"][0]
                        
                        lasers.remove(laser)"""