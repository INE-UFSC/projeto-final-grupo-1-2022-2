import pygame as pg

from ..icontrol import IControl
from .components import Button, Text
from .layout import GridLayout
from .menu import Menu


class StartMenu(Menu):
    def __init__(self, control: IControl):
        components = [
            [Text("Corre Pro RU", 64)],
            [Button("Play")],
            [Button("Leaderboards")],
            [Button("Settings")],
            [Button("Credits")],
            [Button("Quit")],
        ]

        layout = GridLayout(
            components, pg.Vector2(control.screen.size), center_x=True, center_y=True
        )

        super().__init__(control, layout)
