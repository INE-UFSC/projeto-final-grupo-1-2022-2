from abc import ABC
from typing import Dict, List

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

    __components: Dict[
        str, List[MenuComponent]
    ]  # cada elemento corresponde à uma linha do menu
    __control: IControl
    __h_padding: int = 50
    __v_padding: int = 50

    __h_spacing: int = 50
    __v_spacing: int = 100

    def __init__(
        self,
        components: List[List[MenuComponent]],
        control: IControl,
        grid_layout: bool = True,
        center_x: bool = False,
        center_y: bool = False,
    ):
        super().__init__()

        self.__control = control
        for line in components:
            for component in line:
                self.subscribe(component)
                component.event = self.control.event

        if grid_layout:
            components = self.__create_grid_layout(components)
        if center_x:
            self.__center_x(components)
        if center_y:
            self.__center_y(components)

        self.__components = {}
        for line in components:
            for component in line:
                self.__components[component.key] = component

    def render(self):
        # renderiza todos os componentes do menu
        for component in self.__components.values():
            component.render(self.control.screen.display)

    def __create_grid_layout(self, components: List[List[MenuComponent]]) -> None:
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

    def __center_x(self):
        """
        centraliza o eixo x do menu no centro da tela
        """
        ...

    def __center_y(self):
        """
        centraliza o eixo y do menu no centro da tela
        """
        ...

    @property
    def components(self):
        return self.__components

    @property
    def control(self):
        return self.__control

    @components.setter
    def components(self, components: Dict[str, List[MenuComponent]]):
        self.__components = components
