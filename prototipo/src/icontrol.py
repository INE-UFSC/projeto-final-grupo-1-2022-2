from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from .entity import EntityManager, Map
    from .leaderboard import Leaderboard
    from .library import EventBus, Keyboard, Mouse, Screen
    from .scene import Scene
    from .config import Config


class IControl(Protocol):
    config: "Config"
    event: "EventBus"
    keyboard: "Keyboard"
    mouse: "Mouse"
    screen: "Screen"
    leaderboard: "Leaderboard"
    entities: "EntityManager"
    map: "Map"
    deltatime: "float"

    @abstractmethod
    def transition(self, to_scene: "Scene"):
        ...