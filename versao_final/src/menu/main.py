import pygame as pg

from ..dao import LeaderboardDAO
from ..entity import Player
from ..icontrol import IControl
from ..library import Listener
from .components import Text
from .layout import GridLayout
from .menu import Menu
from .render import DefaultRender


class GameplayMenu(Menu):
    __current_speed: int = (
        10  # não leva em conta a velocidade do jogador, é só pra ficar bonito na tela
    )

    def __init__(self, control: IControl):
        components = [
            [Text("Score: 0", font_size=36, key="score")],
            [Text(f"Speed: {self.__current_speed} km/h", key="speed", font_size=36)],
        ]

        layout = GridLayout(
            components, pg.Vector2(control.screen.size), spacing=(50, 50)
        )

        render = DefaultRender(control.screen, components)

        super().__init__(control, layout, render)

    def update(self):
        player_name = LeaderboardDAO().get_player_name()
        if player_name is None:
            player_name = self.control.config.default_player_name
        difficulty = self.control.config.difficulty

        score = LeaderboardDAO().get_player_score()

        text = self.get_component("score")
        text.set_message(f"Score: {str(score)}")

    def render(self):
        self.fresh_render()

    @Listener.on("change player_velocity")
    def __change_speed(self, player_speed: int):
        speed = self.get_component("speed")
        self.__current_speed += 5
        speed.set_message(f"Speed: {self.__current_speed} km/h")

    def leave(self):
        speed = self.get_component("speed")
        speed.set_message("Speed: 10 km/h")
        self.__current_speed = 10
        super().leave()
