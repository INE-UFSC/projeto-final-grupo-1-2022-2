from collections import namedtuple
from typing import List

import pygame as pg

from .components import MenuComponent

All_keys = namedtuple("All_keys", ["keyboard", "mouse"])


class Menu:
    components: List[MenuComponent]

    def __init__(self, components):
        self.__components = components

    def update(self):
        # atualiza todos os componentes do menu
        # com base nas teclas pressionadas e na
        # posição do mouse

        keyboard_keys = pg.key.get_focused()
        mouse_keys = pg.mouse.get_pressed()
        keys = All_keys(keyboard_keys, mouse_keys)

        mouse_pos = pg.Vector2(pg.mouse.get_pos())
        for component in self.__components:
            component.update(keys, mouse_pos)

    def render(self, screen: pg.Surface):
        # renderiza todos os componentes do menu

        for component in self.__components:
            component.render(screen)

    @property
    def components(self):
        return self.__components
