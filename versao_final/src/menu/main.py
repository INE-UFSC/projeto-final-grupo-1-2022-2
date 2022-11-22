from ..entity import Player
from ..icontrol import IControl
from .components import Text
from .menu import Menu


class GameplayMenu(Menu):
    def __init__(self, control: IControl, player: Player):
        ...
