from typing import List

import pygame as pg

from .components import MenuComponent


class Menu:
    __components: List[MenuComponent]

    def __init__(self, components):
        self.__components = components

    def render(self, screen: pg.Surface):
        # renderiza todos os componentes do menu

        for component in self.__components:
            component.render(screen)

    @property
    def components(self):
        return self.__components
