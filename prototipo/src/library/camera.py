from typing import Tuple, Union

import pygame as pg


class Camera:
    __pos: pg.Vector2

    def __init__(self, pos: Union[Tuple[int, int], pg.Vector2] = None):
        if pos is None:
            pos = pg.Vector2(0, 0)

        self.__pos = pos if isinstance(pos, pg.Vector2) else pg.Vector2(pos)

    def update(self):
        ...

    @property
    def pos(self):
        return self.__pos
