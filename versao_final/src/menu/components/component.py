from abc import ABC, abstractmethod
from typing import List, Tuple, Union

import pygame as pg

from ...library import Listener


class MenuComponent(Listener, ABC):
    __pos: Union[pg.Vector2, None]
    __surface: pg.Surface
    __size: pg.Vector2
    __event: Listener
    __key: str

    def __init__(
        self,
        pos: pg.Vector2,
        size: pg.Vector2,
        surface: pg.Surface,
        key: str,
        event_emitter: Listener = None,
    ):
        super().__init__()
        self.__surface = surface
        self.__pos = pg.Vector2(pos) if pos is not None else pos
        self.__size = pg.Vector2(size)
        self.__event = event_emitter
        self.__key = key

    def render(self, screen: pg.Surface):
        if self.__pos is not None:
            screen.blit(self.__surface, self.__pos)

    def is_inside(self, coordinate: Union[pg.Vector2, Tuple[int, int]]) -> bool:
        coordinate = pg.Vector2(coordinate)

        x_min = self.pos.x
        x_max = self.pos.x + self.surface.get_width()
        y_min = self.pos.y
        y_max = self.pos.y + self.surface.get_height()

        return x_min < coordinate.x < x_max and y_min < coordinate.y < y_max

    @property
    def surface(self):
        return self.__surface

    @property
    def size(self):
        return self.__size

    @property
    def event(self):
        return self.__event

    @property
    def pos(self):
        return self.__pos

    @property
    def key(self):
        return self.__key

    @pos.setter
    def pos(self, pos: pg.Vector2):
        self.__pos = pg.Vector2(pos)

    @key.setter
    def key(self, key: str):
        self.__key = key

    @surface.setter
    def surface(self, surface: pg.Surface):
        self.__surface = surface

    @event.setter
    def event(self, event: Listener):
        self.__event = event
