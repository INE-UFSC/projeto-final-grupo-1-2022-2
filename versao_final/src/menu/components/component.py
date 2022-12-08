from abc import ABC, abstractmethod
from typing import List, Tuple, Union

import pygame as pg

from ...library import Listener


class MenuComponent(Listener, ABC):
    _pos: Union[pg.Vector2, None]
    __surface: pg.Surface
    __size: pg.Vector2
    __event: Listener
    __key: str
    __dirty: bool = False
    __spacing: pg.Vector2

    def __init__(
        self,
        pos: pg.Vector2,
        size: pg.Vector2,
        surface: pg.Surface,
        key: str,
        event_emitter: Listener = None,
        spacing: pg.Vector2 = None
    ):
        super().__init__()
        self.__surface = surface
        self._pos = pg.Vector2(pos) if pos is not None else pos
        self.__size = pg.Vector2(size)
        self.__event = event_emitter
        self.__key = key
        self.__spacing = pg.Vector2(0,0) if spacing is None else pg.Vector2(spacing)

    def render(self, screen: pg.Surface):
        if self._pos is not None and self.__dirty:
            screen.blit(self.__surface, self._pos)
            self.__dirty = False
    def fresh_render(self, screen: pg.Surface):
        self.__dirty = True
        self.render(screen)

    def is_inside(self, coordinate: Union[pg.Vector2, Tuple[int, int]]) -> bool:
        coordinate = pg.Vector2(coordinate)

        x_min = self.pos.x
        x_max = self.pos.x + self.surface.get_width()
        y_min = self.pos.y
        y_max = self.pos.y + self.surface.get_height()

        return x_min < coordinate.x < x_max and y_min < coordinate.y < y_max

    def emit_event(self):
        """
        emite um evento nomeado pelo atributo `key` do componente
        """
        self.event.emit(self.key)

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
        return self._pos

    @property
    def key(self):
        return self.__key
    @property
    def dirty(self):
        return self.__dirty
    @property
    def spacing(self):
        return self.__spacing
    

    @pos.setter
    def pos(self, pos: pg.Vector2):
        self._pos = pg.Vector2(pos)
        self.dirty = True
    @dirty.setter
    def dirty(self, dirty: bool):
        self.__dirty = dirty

    @key.setter
    def key(self, key: str):
        self.__key = key

    @surface.setter
    def surface(self, surface: pg.Surface):
        self.__surface = surface

    @event.setter
    def event(self, event: Listener):
        self.__event = event
