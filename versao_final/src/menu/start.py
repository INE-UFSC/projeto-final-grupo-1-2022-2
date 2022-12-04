import pygame as pg

from ..icontrol import IControl
from .components import Button, InputText, Text
from .layout import GridLayout
from .menu import Menu
from .render import BackgroundRender


class StartMenu(Menu):
    def __init__(self, control: IControl):
        components = [
            [Text("Corre Pro RU", font_size=64)],
            [
                Text("Current name: "),
                InputText(
                    control.config.player_name,
                    key="player_name",
                    color="#2A344F",
                    size=(300, 25),
                    word_limit=23,
                ),
            ],
            [Button("Play")],
            [Button("Leaderboards")],
            [Button("Settings")],
            [Button("Credits")],
            [Button("Quit")],
        ]

        layout = GridLayout(
            components,
            pg.Vector2(control.screen.size),
            center_x=True,
            center_y=True,
            spacing=(50, 50),
        )

        render = BackgroundRender(control.screen, components, (0,0,0,175), layout.get_pos(), layout.get_size())

        super().__init__(control, layout, render)
