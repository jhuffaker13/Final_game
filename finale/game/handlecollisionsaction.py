from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

class HandleCollisionsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        physics_service (PhysicsService): An instance of PhysicsService.
    """

    def __init__(self, physics_service, audio_service):
        """The class constructor.
        
        Args:
            physics_service (PhysicsService): An instance of PhysicsService.
        """
        #super().__init__()
        self.physics_service = physics_service
        self.audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        try:
            hero = cast["hero"][0]
            herolist = cast["hero"]
            enemies = cast["enemies"]
            lasers = cast["laser"]
            enemylasers = cast["enemyweapon"]
            for enemy in enemies:
                for laser in lasers:
                    if self.physics_service.is_collision(enemy, laser):
                        lasers.remove(laser)
                        enemy.set_health(enemy.get_health() - laser.get_damage())
                        if enemy.get_health() < 1:
                            enemies.remove(enemy)
                        #print("Hit!")
                        #print(enemy.get_health())

            for enemylaser in enemylasers:
                if self.physics_service.is_collision(enemylaser, hero):
                    enemylasers.remove(enemylaser)
                    hero.set_health(hero.get_health() - 20)
                    if hero.get_health() <= 0:
                        hero.set_health(0)
                        herolist.remove(hero)
                        break
                    health_bar = Actor()
                    health_bar.set_text(f"Health: {hero.get_health()}")
                    health_bar.set_position(Point(1, 0))
                    cast["health_bar"] = [health_bar]
        except KeyError:
            pass

        """ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        if self.physics_service.is_collision(ball, paddle):
            current_x = cast["balls"][0].get_velocity().get_x()
            reverse_y = cast["balls"][0].get_velocity().get_y() * -1
            cast["balls"][0].set_velocity(Point(current_x, reverse_y))

        for brick in bricks:
            if self.physics_service.is_collision(ball, brick):
                current_x = cast["balls"][0].get_velocity().get_x()
                reverse_y = cast["balls"][0].get_velocity().get_y() * -1
                cast["balls"][0].set_velocity(Point(current_x, reverse_y))
                bricks.remove(brick)
                self.audio_service.play_sound(constants.SOUND_BOUNCE)"""
        