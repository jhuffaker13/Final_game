import os

MAX_X = 1600
MAX_Y = 800
FRAME_RATE = 90

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

HERO_ONE = os.path.join(os.getcwd(), "./finale/assets/pixil-frame-1.png")
HERO_TWO = os.path.join(os.getcwd(), "./finale/assets/pixil-frame-2.png")
HERO_THREE = os.path.join(os.getcwd(), "./finale/assets/pixil-frame-3.png")

HERO_ONE_LASER = os.path.join(os.getcwd(), "./finale/assets/bluelaser.png")
HERO_TWO_LASER = os.path.join(os.getcwd(), "./finale/assets/yellowlaser.png")
HERO_THREE_UP_LASER = os.path.join(os.getcwd(), "./finale/assets/upred.png")
HERO_THREE_LASER = os.path.join(os.getcwd(), "./finale/assets/redlaser.png")
HERO_THREE_DOWN_LASER = os.path.join(os.getcwd(), "./finale/assets/downred.png")

ENEMY = os.path.join(os.getcwd(), "./finale/assets/pixil-frame-0.png")

IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
WHITE_LASER = os.path.join(os.getcwd(), "./finale/assets/enemylaser.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

ENEMY_LASER = -7

HERO_LASER = 7

LASER_HEIGHT = 10
LASER_WIDTH = 50

HERO_DX = 8
HERO_DY = HERO_DX * -1

ENEMY_PD = 3
ENEMY_ND = -3
ENEMY_Z = 0

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

HERO_SPEED = 5

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

HERO_WIDTH = 85
HERO_HEIGHT = 80

