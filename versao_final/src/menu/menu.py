from collections import namedtuple
from typing import List

import pygame as pg

from .components import MenuComponent

All_keys = namedtuple("All_keys", ["keyboard", "mouse"])


class Menu:
    components: List[MenuComponent]

    def __init__(self, components):
        self.__components = components

    

    def render(self, screen: pg.Surface):
        # renderiza todos os componentes do menu

        for component in self.__components:
            component.render(screen)

    @property
    def components(self):
        return self.__components
