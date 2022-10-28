from typing import Tuple, Union

import pygame as pg


class Screen:
    size: Tuple[int, int]
    display: Union[pg.Surface, None]

    def __init__(self, size: Tuple[int, int]):
        self.__size = size
        self.__display = None

    def start(self):
        self.__display = pg.display.set_mode(self.__size)

    def update(self):
        pg.display.update()
    
    def get_pos(pos: pg.Vector3 | Tuple[float, float, float]):
        return (pos[0], round(pos[2]) - round(pos[1]))

    @property
    def size(self):
        return self.__size

    @property
    def display(self):
        return self.__display
