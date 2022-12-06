from typing import Union

import pygame as pg

from ..library.collider import CubeCollider
from .component import Component


class RenderComponent(Component):
    def __init__(
        self,
        surface: pg.Surface,
        origin: pg.Vector2 = None,
        alpha: bool = False,
    ):
        size = surface.get_size()
        
        surface = surface.convert_alpha() if alpha else surface.convert()

        if origin is None:
            origin = (size[0] // 2, size[1])

        self.__size = pg.Vector2(size)
        self.__origin = pg.Vector2(origin)
        self.__surface = surface

    @property
    def surface(self):
        return self.__surface

    @property
    def size(self):
        return self.__size

    @property
    def origin(self):
        return self.__origin
