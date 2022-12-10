from argparse import ArgumentParser
from typing import Tuple

from .library import Singleton


class Config(metaclass=Singleton):
    __screen_size: Tuple[int, int] = (1280, 760)

    __difficulty: str = "easy"
    __default_player_name: str = "Graduando Desconhecido"
    __lane_amount: int = 3
    __lane_width: int = 120

    __framerate: int = 60
    __max_deltatime: float = 0.1

    __destruction_distance: int = 1000

    __slide_duration: float = 0.25
    __gravity: float = -1600
    __jump_force: float = 580
    __crouch_duration: int = 1000  # crouch duration in milliseconds

    __camera_y_offset: int = -100

    def __init__(self):
        self.__parse_args()

    def __parse_args(self):
        parser = ArgumentParser()
        parser.add_argument(
            "--save-textures",
            default=False,
            action="store_true",
            help="Save loaded and generated textures.",
        )
        self.__args = parser.parse_args()


    @property
    def args(self):
        return self.__args

    @property
    def screen_size(self):
        return self.__screen_size

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value):
        self.__difficulty = value

    @property
    def default_player_name(self):
        return self.__default_player_name


    @property
    def lane_amount(self):
        return self.__lane_amount

    @property
    def lane_width(self):
        return self.__lane_width

    @property
    def framerate(self):
        return self.__framerate

    @property
    def max_deltatime(self):
        return self.__max_deltatime

    @property
    def destruction_distance(self):
        return self.__destruction_distance

    @property
    def slide_duration(self):
        return self.__slide_duration

    @property
    def gravity(self):
        return self.__gravity

    @property
    def jump_force(self):
        return self.__jump_force

    @property
    def crouch_duration(self):
        return self.__crouch_duration

    @property
    def camera_y_offset(self):
        return self.__camera_y_offset
