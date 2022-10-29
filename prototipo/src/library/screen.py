from typing import Tuple, Union

import pygame as pg

from .camera import Camera


class Screen:
    __size: Tuple[int, int]
    __display: Union[pg.Surface, None]
    __cam: Camera

    def __init__(self, size: Tuple[int, int], camera: Union[Camera, None] = None):
        self.__size = size
        self.__display = None
        self.__cam = Camera()

    def start(self):
        self.__display = pg.display.set_mode(self.__size)

    def update(self):
        pg.display.update()

    def get_pos(self, pos: Union[pg.Vector3, Tuple[float, float, float]]):
        x = pos[0] - self.__cam.pos[0]
        y = self.size[1] - (pos[1] + pos[2] - self.__cam.pos[1])

        return (round(x), round(y))

    @property
    def size(self):
        return self.__size

    @property
    def display(self):
        return self.__display

    @property
    def cam(self):
        return self.__cam
