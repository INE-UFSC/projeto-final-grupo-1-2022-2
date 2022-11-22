import pygame as pg

from ..icontrol import IControl
from .components import Button, Text
from .menu import Menu


class StartMenu(Menu):
    def __init__(self, control: IControl):
        components = [
            [Text("Corre Pro RU", 64)],
            [Button("Play")],
            [Button("Leaderboards")],
            [Button("Settings")],
            [Button("Credits")],
            [Button("Quit")],
        ]
        super().__init__(components, control, True)
