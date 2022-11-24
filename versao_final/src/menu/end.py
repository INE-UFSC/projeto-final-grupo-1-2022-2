import pygame as pg

from ..icontrol import IControl
from .components import Button, Image, Text
from .layout import GridLayout
from .menu import Menu


class EndMenu(Menu):
    def __init__(self, control: IControl):

        components = [
            [Text("Game Over", 48)],
            [Button("Play again", key="Play", size=(550, 50))],
            [Button("Return to start menu", key="Start"), Button("Quit")],
        ]

        layout = GridLayout(
            components,
            control.screen.size,
            pg.Vector2(50, 75),
            center_x=True,
            center_y=True,
        )

        super().__init__(control, layout, (0, 0, 0), (40, 40, 40, 10))
