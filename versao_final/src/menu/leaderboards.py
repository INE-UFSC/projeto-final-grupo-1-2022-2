from typing import List

from ..dao import LeaderboardDAO
from ..icontrol import IControl
from .components import Button, Text
from .layout import GridLayout
from .menu import Menu
from .render import BackgroundRender


class LeaderBoardMenu(Menu):

    __current_page: int = 1
    __previous_page: int = 0
    __page_limit: int

    def __init__(
        self,
        control: IControl,
    ):

        components = [
            [Text("Leaderboard", font_size=64, size=(358, 150))],
            *(
                [
                    Text(f"{i}.", key=f"name_{i}", size=(800, 25)),
                    Text("x", key=f"score_{i}", size=(150, 25)),
                ]
                for i in range(1, 5)
            ),
            [
                Button(
                    "<-",
                    key="previous",
                    size=(50, 25),
                    on_click=lambda: self.__decrement_page(),
                ),
                Text("5.", size=(800, 25), key="name_5"),
                Text("x", size=(150, 25), key="score_5"),
                Button(
                    "->",
                    key="next",
                    size=(50, 25),
                    on_click=lambda: self.__increment_page(),
                ),
            ],
            *(
                [
                    Text(f"{i}.", key=f"name_{i}", size=(800, 25)),
                    Text("x", key=f"score_{i}", size=(150, 25)),
                ]
                for i in range(6, 11)
            ),
            [Button("Return to start menu")],
        ]

        layout = GridLayout(
            components,
            control.screen.size,
            center_x=True,
            center_y=True,
        )

        render = BackgroundRender(control.screen, components, (0,0,0,175), layout.get_pos(), layout.get_size())

        super().__init__(control, layout, render)

    def enter(self):
        super().enter()
        self.__page_limit = (
            1 + len(LeaderboardDAO()._cache.get("players", {}).values()) // 10
        )

    def leave(self):
        super().leave()
        self.__current_page = 1
        self.__previous_page = 0

    def update(self):

        if self.__current_page != self.__previous_page:
            self._dirty = True
            self.__previous_page = self.__current_page
            players = LeaderboardDAO().get_sorted_list(self.control.config.difficulty)
            lower_limit = 1 + (self.__current_page - 1) * 10
            upper_limit = 10 + (self.__current_page - 1) * 10

            for menu_position, rank_position in enumerate(
                range(lower_limit, upper_limit + 1)
            ):
                name = self.get_component(f"name_{menu_position+1}")
                score = self.get_component(f"score_{menu_position+1}")

                if rank_position - 1 < len(players):
                    player = players[rank_position - 1]

                    name.set_message(f"{rank_position}. {player.name}")
                    score.set_message(f"{player.value}")
                    continue

                name.set_message(f"{rank_position}. ")
                score.set_message("")

    def __increment_page(self):
        if self.__current_page < self.__page_limit:
            self.__current_page += 1

    def __decrement_page(self):
        if self.__current_page != 1:
            self.__current_page -= 1
