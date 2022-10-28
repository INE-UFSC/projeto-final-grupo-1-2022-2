from .component import Component
from pygame import Vector2
import pygame as pg

class RenderComponent(Component):
    def __init__(self, size: Vector2, color: str):
        self.__size = pg.Vector2(size)
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
    def color(self):
        return self.__color