import pygame as pg

from .component import Component


class RenderComponent(Component):
    def __init__(self, size: pg.Vector2, color: str, origin: pg.Vector2 = None):
        if origin is None:
            origin = (size[0] // 2, size[1])

        self.__size = pg.Vector2(size)
        self.__origin = pg.Vector2(origin)
        self.__surface = pg.Surface(size)
        self.__color = color

        self.__surface.fill(self.__color)

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
