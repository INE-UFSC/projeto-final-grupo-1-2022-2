import pygame as pg

from ..icontrol import IControl
from .components import Button, Image, Text
from .layout import GridLayout
from .menu import Menu
from .render import TransparencyBackgroundRender
from ..dao import LeaderboardDAO

class EndMenu(Menu):
    def __init__(self, control: IControl):

        components = [
            [Text("Game Over", font_size=48)],
            [Text("Score: ", key="score")],
            [Button("Play again", key="Play", size=(550, 50))],
            [Button("Return to start menu", key="Start"), Button("Quit")],
        ]

        layout = GridLayout(
            components,
            control.screen.size,
            center_x=True,
            center_y=True,
        )

        render = TransparencyBackgroundRender(control.screen, components, "black", layout.get_pos(), layout.get_size(), (40,40,40,10), True)

        super().__init__(control, layout, render)

    def enter(self):
        player_score = LeaderboardDAO().get_player_score()
        score = self.get_component("score")
        score.set_message(f"Score: {player_score}")