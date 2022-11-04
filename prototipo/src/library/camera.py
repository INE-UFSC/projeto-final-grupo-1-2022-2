from typing import Tuple, Union

import pygame as pg


class Camera:
    __pos: pg.Vector2
    __offset = pg.Vector2

    def __init__(
        self,
        pos: Union[Tuple[int, int], pg.Vector2] = None,
        offset: Union[pg.Vector2, Tuple[int, int]] = None,
    ):
        if pos is None:
            pos = pg.Vector2(0, 0)

        if offset is None:
            offset = pg.Vector2(0, -100)

        self.__pos = pos if isinstance(pos, pg.Vector2) else pg.Vector2(pos)
        self.__offset = offset

    def update(self, pos: Union[pg.Vector2, Tuple[int, int]]):
        pos = pg.Vector2(pos)

        self.__pos.x = pos.x + self.__offset.x
        self.__pos.y = pos.y + self.__offset.y

    @property
    def pos(self):
        return self.__pos
