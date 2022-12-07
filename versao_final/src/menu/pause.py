import pygame as pg

from ..icontrol import IControl
from .components import Button, Text
from .layout import GridLayout
from .menu import Menu
from .render import TransparencyBackgroundRender

class PauseMenu(Menu):

    def __init__(self, control: IControl):
        components = [
            [Text("Paused",font_size=48)],
            [Button("Resume")],
            [Button("Quit")],
        ]

        layout = GridLayout(
            components,
            pg.Vector2(control.screen.size),
            center_x=True,
            center_y=True,
        )

        render = TransparencyBackgroundRender(control.screen, components, (0,0,0), layout.get_pos(), layout.get_size(), (40,40,40,10),True)

        super().__init__(control, layout, render)
