from typing import Union

import pygame as pg


class Screen:
    __size: tuple[int, int]
    __display: Union[pg.Surface, None]

    def __init__(self, size: tuple[int, int]):
        self.__size = size
        self.__display = None

    def start(self):
        self.__display = pg.display.set_mode(self.__size)

    def update(self):
        pg.display.update()

    @property
    def size(self):
        return self.__size

    @property
    def display(self):
        return self.__display
