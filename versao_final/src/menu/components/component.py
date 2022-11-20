from abc import ABC, abstractmethod
from typing import List, Tuple

from pygame import Surface, Vector2

from ...library import Listener


class MenuComponent(ABC, Listener):
    __pos: Vector2
    __surface: Surface

    def __init__(self, pos: Vector2, surface: Surface):
        self.__pos = pos
        self.__surface = surface

    def render(self, screen: Surface):
        screen.blit(self.__surface, self.__pos)

    @property
    def pos(self):
        return self.__pos

    @property
    def surface(self):
        return self.__surface
