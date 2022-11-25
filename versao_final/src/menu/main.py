import pygame as pg

from ..entity import Player
from ..icontrol import IControl
from .components import Text
from .layout import GridLayout
from .menu import Menu


class GameplayMenu(Menu):
    def __init__(self, control: IControl):
        components = [[Text("Score: 0", 36, key="score")], [Text("Speed: 0 km/h", 36)]]

        layout = GridLayout(components, pg.Vector2(control.screen.size))

        super().__init__(control, layout)
