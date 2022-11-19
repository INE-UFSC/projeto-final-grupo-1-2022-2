from typing import Union

import pygame as pg

from ..library.collider import CubeCollider
from .component import Component


class RenderComponent(Component):
    def __init__(
        self,
        size: pg.Vector2,
        color: Union[str, pg.Color],
        origin: pg.Vector2 = None,
        surface: pg.Surface = None,
    ):
        if origin is None:
            origin = (size[0] // 2, size[1])

        self.__size = pg.Vector2(size)
        self.__origin = pg.Vector2(origin)
        self.__color = color if isinstance(surface, pg.Surface) else pg.Color(color)

        if isinstance(surface, pg.Surface):
            self.__surface = surface
        else:
            self.__surface = pg.Surface(size)
            self.__surface.fill(self.__color)

    @classmethod
    def from_cube(cls, cube: CubeCollider, color: Union[str, pg.Color]):
        size = cube.size
        surface_size = (size[0], size[1] + size[2])

        color = pg.Color(color)
        shade_color = [int(c * 0.6) for c in color[:3]]

        surface = pg.Surface(surface_size)
        surface.fill(color)
        pg.draw.rect(
            surface,
            shade_color,
            (0, surface_size[1] - size[1], surface_size[0], size[1]),
        )

        return cls(surface_size, color, surface=surface)

    @property
    def surface(self):
        return self.__surface

    @property
    def size(self):
        return self.__size

    @property
    def origin(self):
        return self.__origin

    @property
    def color(self):
        return self.__color
