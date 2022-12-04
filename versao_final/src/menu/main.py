import pygame as pg

from ..dao import LeaderboardDAO
from ..entity import Player
from ..icontrol import IControl
from .components import Text
from .layout import GridLayout
from .menu import Menu
from .render import DefaultRender


class GameplayMenu(Menu):
    def __init__(self, control: IControl):
        components = [
            [Text("Score: 0", font_size=36, key="score")],
            [Text("Speed: 0 km/h", font_size=36)],
        ]

        layout = GridLayout(
            components, pg.Vector2(control.screen.size), spacing=(50, 50)
        )

        render = DefaultRender(control.screen, components)

        super().__init__(control, layout, render)

    def update(self):
        player_name = LeaderboardDAO().get_player_name()
        difficulty = self.control.config.difficulty

        score = LeaderboardDAO()._cache["players"][player_name][difficulty]["highscore"]

        text = self.get_component("score")
        text.set_message(f"Score: {str(score)}")

    def render(self):
        self.fresh_render()