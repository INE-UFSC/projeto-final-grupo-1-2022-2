import pygame as pg

from ..icontrol import IControl
from .components import Button, Text
from .layout import GridLayout
from .menu import Menu


class PauseMenu(Menu):
    __background_color = "black"
    __background: pg.Surface

    __transparent_layer: pg.Surface
    __transparent_color = (40, 40, 40, 10)

    def __init__(self, control: IControl):
        components = [
            [
                Button("Resume", size=(550, 50)),
            ],
            [Button("Settings"), Button("Quit")],
        ]

        layout = GridLayout(
            components,
            pg.Vector2(control.screen.size),
            center_x=True,
            center_y=True,
            spacing=pg.Vector2(50, 75),
        )

        super().__init__(control, layout)

        self.__background = pg.Surface(self.size)
        self.__transparent_layer = pg.Surface(self.control.screen.size, pg.SRCALPHA)

    def render(self):
        self.__transparent_layer.fill(self.__transparent_color)
        self.__background.fill(self.__background_color)
        self.__transparent_layer.blit(self.__background, self.pos)
        for component in self.layout.get_all_components():
            component.render(self.__transparent_layer)

        self.control.screen.display.blit(self.__transparent_layer, (0, 0))
