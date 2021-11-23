import raylibpy
from game.change_color import ChangeColor
from game.control_actors_action import ControlActorsAction
from game.actor import Actor
from game import constants

class Hero(Actor):
    def __init__(self):
        super().__init__()
        self.change_color = ChangeColor
        self.set_width(constants.HERO_WIDTH)
        self.set_height(constants.HERO_HEIGHT)
        if self.change_color.execute == 1:
            self.set_image(constants.HERO_THREE)
        else:  
            self.set_image(constants.HERO_TWO)
        

    def change_color(self):
        self.set_image = self.change_color.execute()

    