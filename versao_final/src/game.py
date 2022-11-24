from os import chdir

import pygame as pg

from .control import GameControl
from .scene import EndScene, MainScene, StartScene


class Game:
    control: GameControl

    def __init__(self):
        pg.init()
        control = GameControl()
        self.__control = control

        control.scene.add(
            start=StartScene(control),
            main=MainScene(control),
            end=EndScene(control),
        )
        control.scene.transition("start")

    def start(self):
        self.__control.start()

        self.__loop()

    def __loop(self):
        while self.__control.is_running():
            self.__control.update()


def run_game(path: str = None):
    if path:
        chdir(path)

    game = Game()

    game.start()
