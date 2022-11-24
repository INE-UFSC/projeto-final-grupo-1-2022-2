from abc import ABC
from typing import Tuple, Union

import pygame as pg

from ..icontrol import IControl
from ..library import Listener
from .layout import Layout
from .render import (
    BackgroundRender,
    DefaultRender,
    Render,
    TransparencyBackgroundRender,
)

# TODO
# substituir o control por outros parâmetros
# adicionar opção de mudar a cor de fundo do menu
# renderizar o menu só quando necessário


class Menu(ABC, Listener):
    __control: IControl
    __layout: Layout
    __pos: pg.Vector2
    __size: pg.Vector2
    __render: Render

    def __init__(
        self,
        control: IControl,
        layout: Layout,
        bg_color: Union[str, pg.Color] = None,
        transparency_color: Union[pg.Color, Tuple[int, int, int, int]] = None,
    ):
        """
        classe base para os menus do jogo

        parâmetros:
        - `control`: controlador do jogo;
        - `layout`: layout usado no menu do jogo;
        - `bg_color`: cor do fundo do menu;
        - `transparency_color`: cor usada para conferir transparencia ao menu, deve possuir um valor alpha
        """

        super().__init__()
        self.__layout = layout
        self.__control = control
        self.__pos = self.__layout.get_pos()
        self.__size = self.__layout.get_size()

        screen = self.__control.screen
        components = self.__layout.get_all_components()

        # menu sem transparência ou cor de fundo
        if bg_color is None and transparency_color is None:
            self.__render = DefaultRender(screen, components)

        # menu com cor de fundo
        elif bg_color is not None and transparency_color is None:
            self.__render = BackgroundRender(
                screen, components, bg_color, self.__pos, self.__size
            )

        # menu com cor de fundo e transparência
        else:
            self.__render = TransparencyBackgroundRender(
                screen,
                components,
                bg_color,
                self.__pos,
                self.__size,
                transparency_color,
            )

        for component in self.__layout.get_all_components():
            self.subscribe(component)
            component.event = self.control.event

    def render(self):
        # renderiza todos os componentes do menu
        self.__render.render()

    @property
    def pos(self):
        return self.__pos

    @property
    def size(self):
        return self.__size

    @property
    def control(self):
        return self.__control

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout: Layout):
        self.__layout = layout
