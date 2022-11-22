from abc import ABC
from typing import List

import pygame as pg

from ..icontrol import IControl
from ..library import Listener
from .components import MenuComponent


# TODO
# função para instanciar o menu no centro da tela
# Menu de opções
# Menu exibido durante a gameplay
# menu de créditos
# menu de pausa
# menu final
class Menu(ABC, Listener):

    __components: List[
        List[MenuComponent]
    ]  # cada elemento corresponde à uma linha do menu
    __control: IControl
    __h_padding: int = 50
    __v_padding: int = 50

    __h_spacing: int = 50
    __v_spacing: int = 100

    def __init__(self, components: List[List[MenuComponent]], control: IControl):
        super().__init__()
        self.__components = components
        self.__control = control
        for line in self.__components:
            for component in line:
                self.subscribe(component)
                component.event = self.control.event

    def render(self):
        # renderiza todos os componentes do menu
        for line in self.__components:
            for component in line:
                component.render(self.control.screen.display)

    def create_grid_layout(
        self,
        components: List[List[MenuComponent]],
    ) -> List[List[MenuComponent]]:
        """
        cria um grid com os `components` por meio da
        alteração da posição destes
        """
        screen_size = pg.Vector2(self.control.screen.size)
        for i, line in enumerate(components):
            y_pos = self.__v_padding + i * self.__v_spacing

            for j, component in enumerate(line):
                size = component.size
                x_pos = self.__h_padding + j * self.__h_spacing
                component.pos = (x_pos, y_pos)
        return components

    @property
    def components(self):
        return self.__components

    @property
    def control(self):
        return self.__control

    @components.setter
    def components(self, components: List[List[MenuComponent]]):
        self.__components = components
