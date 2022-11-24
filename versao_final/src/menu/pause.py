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

        super().__init__(control, layout, (0, 0, 0), (40, 40, 40, 10))
