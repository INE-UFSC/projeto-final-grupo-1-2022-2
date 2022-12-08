from functools import cache
from typing import Iterable, Union

import pygame as pg

from .component import Component


class RenderComponent(Component):
    def __init__(
        self,
        alpha: bool = False,
        **frames: pg.Surface,
    ):
        self.__frames = frames
        self.__alpha = alpha
        self.__current = None
        self.__current_id = None
        self.__duration = 0.1
        self.__index = 0

        self.set_frame("default")
    
    def set_frame(self, name: str):
        if name == self.__current_id: return

        frame = self.__frames.get(name)

        self.__index = 0
        self.__timer = 0
        self.__current = self.convert(frame)
        self.__current_id = name
    
    def set_duration(self, value: float):
        self.__duration = value
    
    @cache
    def convert(self, value: Union[pg.Surface, Iterable[pg.Surface]]):
        if isinstance(value, Iterable):
            return [self.convert(v) for v in value]
        return value.convert_alpha() if self.__alpha else value.convert()
    
    def update(self, deltatime: float):
        if isinstance(self.__current, Iterable):
            self.__timer += deltatime
            if self.__timer >= self.__duration:
                self.__index = (self.__index + 1) % len(self.__current)
                self.__timer = 0

    @property
    def surface(self):
        return self.__current[self.__index] if isinstance(self.__current, Iterable) else self.__current

    @property
    def size(self):
        return pg.Vector2(self.surface.get_size())

    @property
    def origin(self):
        size = self.size
        return pg.Vector2(size[0] // 2, size[1])
