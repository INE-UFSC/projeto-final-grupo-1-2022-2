import pygame as pg

from ..icontrol import IControl
from .components import Button, InputText, Text, Image
from .layout import GridLayout
from .menu import Menu
from .render import BackgroundRender


class TutorialMenu(Menu):
    def __init__(self, control: IControl):

        components = [
            [Text("How to PLAY:", font_size=64, spacing=(0, 10))],
            [
                Text("Use the arrow keys to control your player:", font_size=24),
                Image("menu/arrowk.png"),
            ],
            [Text("Dodge or jump the obstacles in the 3 lanes! ", font_size=24)],
            [Text("Press ESC to pause the game", font_size=24)],
            [Text("Have fun!", font_size=24)],
            [Button("Return to start menu")],
        ]

        layout = GridLayout(
            components,
            pg.Vector2(control.screen.size),
            center_x=True,
            center_y=True,
            spacing=(50, 10),
        )

        render = BackgroundRender(
            control.screen,
            components,
            (0, 0, 0, 175),
            layout.get_pos(),
            layout.get_size(),
        )

        super().__init__(control, layout, render)
