import os


os.environ['RAYLIB_BIN_PATH'] = '.'
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.weapon import Weapon
from game.heroweapon import HeroWeapon
from game.enemyweapon import EnemyWeapon
from game.createenemy import CreateEnemy
from game.hero import Hero
from game.change_color import ChangeColor
from game.enemy import Enemy
from game.random_movement import RandomMovements
from game.control_actors_action import ControlActorsAction
from game.handlecollisionsaction import HandleCollisionsAction
from game.handleoffscreenaction import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.background import Background

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    #This displays a box where the hero is. Simply for testing certain things
    """cast["box"] = []
    boxlist = []
    box = Actor()
    position = Point(600, 300)
    box.set_velocity(Point(0,0))
    box.set_width(constants.HERO_WIDTH)
    box.set_height(constants.HERO_HEIGHT)
    box.set_position(position)
    boxlist.append(box)
    cast["box"] = boxlist"""

    #Background test
    """cast["background"] = []
    backgroundlist = []
    sky = Background()
    sky.set_width(constants.MAX_X)
    sky.set_height(constants.MAX_Y)
    sky.set_image(constants.NIGHT_SKY)
    position = Point(0, 0)
    sky.set_position(position)
    sky.set_velocity(Point(0,0))

    backgroundlist.append(sky)
    cast["background"] = backgroundlist"""  

    cast["hero"] = []
    herolist = []
    hero = Hero() 
    hero.set_image(constants.HERO_ONE)
    hero.set_weapon(1)
    position = Point(600, 300)
    hero.set_position(position)
    hero.set_velocity(Point(constants.HERO_DX, constants.HERO_DY))
    health_bar = Actor()
    health_bar.set_text(f"Health: {hero.get_health()}")
    health_bar.set_position(Point(1, 0))
    cast["health_bar"] = [health_bar]
    herolist.append(hero)
    cast["hero"] = herolist

    
    cast["enemies"] = []
    enemies = []
    for i in range (8):
        enemy = Enemy()
        position = Point(1300, constants.MAX_Y-(i*100)-100)
        enemy.set_position(position)
        enemies.append(enemy)
    cast["enemies"] = enemies


    
    cast["laser"] = []

    


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    hero_number = 2
    weapon_number = 2

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    change_color = ChangeColor(input_service, hero_number)
    weapon = Weapon(input_service, hero_number)
    handleoffscreenaction = HandleOffScreenAction()
    handlecollisionsaction = HandleCollisionsAction(physics_service, audio_service)
    randommovements = RandomMovements()
    heroweapon = HeroWeapon(input_service)
    enemyweapon = EnemyWeapon()
    createenemy = CreateEnemy()
    background = Background()

    

    script["input"] = [control_actors_action, change_color, heroweapon]
    script["update"] = [handleoffscreenaction, handlecollisionsaction, randommovements, createenemy]
    script["output"] = [draw_actors_action, move_actors_action, enemyweapon]



    # Start the game
    output_service.open_window("Finale");
    #audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()
