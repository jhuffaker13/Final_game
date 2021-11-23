from game import constants
from game.action import Action


class ChangeColor():
    def __init__(self, input_service, hero_number):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self.hero_number = hero_number



    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        
        if self._input_service.is_f_pressed():
            if self.hero_number == 1:
            #self._input_service.is_space_pressed() = False
                cast["hero"][0].set_image(constants.HERO_ONE)
                cast["hero"][0].set_weapon(1)

                self.hero_number = 2

                #return hero_image
            elif self.hero_number == 2:
                cast["hero"][0].set_image(constants.HERO_TWO)
                cast["hero"][0].set_weapon(2)

                self.hero_number = 3

                #return hero_image
            elif self.hero_number == 3:
                cast["hero"][0].set_image(constants.HERO_THREE)
                cast["hero"][0].set_weapon(3)
                #print(cast["hero"][0].get_weapon())

                self.hero_number = 1

                #return hero_image

            else:
                self.hero_number = 1