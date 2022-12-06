"""
Classe pos component
"""
from typing import Tuple, Union

import pygame as pg

from .component import Component


class PosComponent(Component):
    value: pg.Vector3

    def __init__(self, value: Union[Tuple[float, float, float], pg.Vector3]):
        self.__value = value if isinstance(value, pg.Vector3) else pg.Vector3(value)

    @property
    def value(self):
        return self.__value
