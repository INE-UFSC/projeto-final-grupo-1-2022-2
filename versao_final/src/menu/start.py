import pygame as pg

from ..dao import LeaderboardDAO
from ..icontrol import IControl
from .components import Button, InputText, Text
from .layout import GridLayout
from .menu import Menu
from .render import BackgroundRender


class StartMenu(Menu):
    def __init__(self, control: IControl):
        player_name = LeaderboardDAO().get_player_name()
        if player_name is None:
            player_name = control.config.default_player_name
        
        components = [
            [Text("Corre Pro RU", font_size=64)],
            [
                Text("Current name: "),
                InputText(
                    player_name,
                    key="player_name",
                    color="#2A344F",
                    size=(250, 25),
                    word_limit=23,
                ),
            ],
            [Button("Play",size=(200,50))],
            [Button("Leaderboards",size=(200,50))],
            [Button("Tutorial",size=(200,50))],
            [Button("Credits",size=(200,50))],
            [Button("Quit",size=(200,50))],
        ]

        layout = GridLayout(
            components,
            pg.Vector2(control.screen.size),
            center_x=True,
            center_y=True,
            spacing=(50, 50),
            pos=(50,None),
            padding=(25,25)
        )

        render = BackgroundRender(control.screen, components, (0,0,0,175), layout.get_pos(), layout.get_size())

        super().__init__(control, layout, render)
