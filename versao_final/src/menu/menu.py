from abc import ABC
from typing import Tuple, Union

import pygame as pg

from ..icontrol import IControl
from ..library import Listener
from .components import MenuComponent
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
    __layouts: Layout
    __pos: pg.Vector2
    __size: pg.Vector2
    __render_strategy: Render
    _dirty: bool = True

    def __init__(
        self,
        control: IControl,
        layout: Layout,
        render: Render,
    ):

        super().__init__()
        self.__layout = layout
        self.__control = control
        self.__pos = self.__layout.get_pos()
        self.__size = self.__layout.get_size()

        screen = self.__control.screen
        components = self.__layout.get_all_components()

        self.__render_strategy = render

        for component in self.__layout.get_all_components():
            self.subscribe(component)
            component.event = self.control.event

    def render(self):
        # renderiza todos os componentes do menu
        if self._dirty:
            self._dirty = False
            self.fresh_render()

        
        self.__render_strategy.render()

    def fresh_render(self):
        self.control.event.emit("menu fresh_render")
        self.__render_strategy.fresh_render()

    def get_component(self, key: str) -> Union[MenuComponent, None]:
        return self.__layout.get_component(key)

    def update(self):
        ...

    def enter(self):
        self._dirty = True
        self.__render_strategy.setup()

    def leave(self):
        self.__render_strategy.reset()
        self._dirty = True

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

    @property
    def render_strategy(self):
        return self.__render_strategy

    @layout.setter
    def layout(self, layout: Layout):
        self.__layout = layout
