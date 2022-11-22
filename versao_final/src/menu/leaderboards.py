from typing import List

from ..icontrol import IControl
from ..leaderboard import Leaderboard
from .components import Button, Text
from .menu import Menu


class LeaderBoardMenu(Menu):
    def __init__(
        self,
        control: IControl,
        leaderboard: Leaderboard,
    ):
        self.__leaderboard = leaderboard

        components = [[Text("Leaderboard", 64)]]

        for name, score in leaderboard.scores:
            components.append([Text(f"{name} - {score}")])

        components.append([Button("Retornar")])
        super().__init__(components, control)
