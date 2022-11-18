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
        self.__is_crouched = False

    @property
    def pos(self):
        return self.__pos

    @property
    def velocity(self):
        return self.__velocity

    @property
    def on_ground(self):
        return self.velocity.y == 0
    
    @property
    def is_crouched(self):
        return self.__is_crouched
    
    @is_crouched.setter
    def is_crouched(self, is_crouched: bool):
        self.__is_crouched = is_crouched
