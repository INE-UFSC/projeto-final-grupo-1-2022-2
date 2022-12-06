"""
Classe move component
"""
from typing import Tuple, Union

import pygame as pg

from .component import Component


class MoveComponent(Component):
    velocity: pg.Vector3

    def __init__(self, velocity):
        self.__velocity = pg.Vector3(velocity)

    @property
    def velocity(self):
        return self.__velocity

    @property
    def on_ground(self):
        return self.velocity.y == 0
