import pygame as pg

from ..dao import LeaderboardDAO
from ..entity import Player
from ..icontrol import IControl
from .components import Text
from .layout import GridLayout
from .menu import Menu
from .render import DefaultRender
from ..library import Listener


class GameplayMenu(Menu):
    def __init__(self, control: IControl):
        components = [
            [Text("Score: 0", font_size=36, key="score")],
            [Text("Speed: 0 km/h", key="speed",font_size=36)],
        ]

        layout = GridLayout(
            components, pg.Vector2(control.screen.size), spacing=(50, 50)
        )

        render = DefaultRender(control.screen, components)

        super().__init__(control, layout, render)

    def update(self):
        player_name = LeaderboardDAO().get_player_name()
        difficulty = self.control.config.difficulty

        score = LeaderboardDAO().get_player_score()

        text = self.get_component("score")
        text.set_message(f"Score: {str(score)}")

    def render(self):
        self.fresh_render()

    @Listener.on("change player_velocity")
    def __change_speed(self, player_speed: int):
        speed = self.get_component("speed")
        speed.set_message(f"Speed: {player_speed / 50} km/h")