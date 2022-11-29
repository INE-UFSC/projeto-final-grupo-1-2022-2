from typing import Tuple
from argparse import ArgumentParser

from .library import Singleton


class Config(metaclass=Singleton):
    
    
    screen_size: Tuple[int, int] = (1280, 760)

    __difficulty: str = "easy"
    __player_name: str = "Graduando Desconhecido"
    
    lane_amount: int = 3
    lane_width: int = 120

    framerate: int = 60
    max_deltatime: float = 0.1

    destruction_distance: int = 1000

    slide_duration: float = 0.25
    gravity: float = -1600
    jump_force: float = 580
    crouch_duration: int = 1000  # crouch duration in milliseconds

    camera_y_offset: int = -100

    def __init__(self): self.__parse_args()
    def __parse_args(self):
        parser = ArgumentParser()
        parser.add_argument("--save-textures", default=False, action="store_true", help="Save loaded and generated textures.")
        self.__args = parser.parse_args()
    @property
    def args(self): return self.__args
    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value):
        self.__difficulty = value


    @property
    def player_name(self):
        return self.__player_name

    @player_name.setter
    def player_name(self, value):
        self.__player_name = value

