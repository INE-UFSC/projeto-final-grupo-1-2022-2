from abc import ABC
from typing import Dict, List

import pygame as pg

from ..icontrol import IControl
from ..library import Listener
from .layout import Layout

# TODO
# Menu de opções
# Menu exibido durante a gameplay
# menu de créditos
# menu de pausa
# menu final


class Menu(ABC, Listener):
    __control: IControl
    __layout: Layout

    def __init__(
        self,
        control: IControl,
        layout: Layout,
    ):
        """
        classe base para os menus do jogo

        parâmetros:
        - `control`: controlador do jogo;
        - `layout`: layout usado no menu do jogo;
        """

        super().__init__()
        self.__layout = layout
        self.__control = control

        for component in self.__layout.get_all_components():
            self.subscribe(component)
            component.event = self.control.event

    def render(self):
        # renderiza todos os componentes do menu
        for component in self.__layout.get_all_components():
            component.render(self.control.screen.display)

    @property
    def control(self):
        return self.__control

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout: Layout):
        self.__layout = layout
