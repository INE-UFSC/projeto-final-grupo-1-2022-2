from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from .entity import EntityManager
    from .leaderboard import Leaderboard
    from .library import EventBus, Keyboard, Mouse, Screen
    from .scene import Scene


class IControl(Protocol):
    event: "EventBus"
    keyboard: "Keyboard"
    mouse: "Mouse"
    screen: "Screen"
    leaderboard: "Leaderboard"
    entities: "EntityManager"
    deltatime: "float"

    @abstractmethod
    def transition(self, to_scene: "Scene"):
        ...