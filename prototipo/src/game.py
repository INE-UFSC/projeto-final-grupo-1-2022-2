from os import chdir

from .control import GameControl
from .scene import MainScene, StartScene


class Game:
    control: GameControl

    def __init__(self):
        control = GameControl()
        self.__control = control

        control.scene.add(
            start=StartScene(control, play_scene="main"),
            main=MainScene(control),
        )
        control.scene.transition("start")

    def start(self):
        self.__control.start()

        self.__loop()

    def __loop(self):
        while self.__control.is_running():
            self.__control.update()


def run_game(path: str = None):
    if path is not None:
        chdir(path)

    game = Game()

    game.start()
