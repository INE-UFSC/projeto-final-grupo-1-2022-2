from typing import List

from ..dao import LeaderboardDAO
from ..icontrol import IControl
from .components import Button, Text
from .menu import Menu


class LeaderBoardMenu(Menu):
    def __init__(
        self,
        control: IControl,
    ):

        components = [[Text("Leaderboard", 64)]]


        components.append([Button("Retornar")])
        super().__init__(components, control)
