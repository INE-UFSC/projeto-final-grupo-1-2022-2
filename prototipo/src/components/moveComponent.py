"""
Classe move component
"""
from typing import Tuple, Union

import pygame as pg

from .component import Component


class MoveComponent(Component):
    pos: pg.Vector3
    velocity: pg.Vector3

    def __init__(self, pos, velocity):
        self.__pos = pg.Vector3(pos)
        self.__velocity = pg.Vector3(velocity)

    @property
    def pos(self):
        return self.__pos

    @property
    def velocity(self):
        return self.__velocity

    @property
    def on_ground(self):
        return self.velocity.y == 0
