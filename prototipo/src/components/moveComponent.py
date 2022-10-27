"""
Classe move component
"""
import pygame as pg

from .component import Component


class MoveComponent(Component):
    pos: pg.Vector3
    velocity: pg.Vector3
    on_ground: bool

    def __init__(self, pos, velocity, on_ground):
        self.__pos = pg.Vector3(pos)
        self.__velocity = pg.Vector3(velocity)
        self.__on_ground = on_ground

    @property
    def pos(self):
        return self.__pos

    @property
    def velocity(self):
        return self.__velocity

    @property
    def on_ground(self):
        return self.__on_ground
