from os import chdir

from .control import GameControl


class Game:
    control: GameControl

    def start(self):
        ...

    def __loop(self):
        ...


def run_game(path: str = None):
    if path is not None:
        chdir(path)

    game = Game()

    game.start()
