from typing import Dict

from .entity import EntityManager
from .event import EventBus
from .keyboard import Keyboard
from .leaderboard import Leaderboard
from .mouse import Mouse
from .scene import IControl, Scene


class GameControl(IControl):
    event: EventBus
    keyboard: Keyboard
    mouse: Mouse
    scenes: Dict[str, Scene]
    current_scene: Scene
    leaderboard: Leaderboard
    entities: EntityManager

    def play(self):
        ...

    def pause(self):
        ...
