from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .config import Config
    from .entity import EntityManager, Map
    from .library import EventBus, Screen
    from .scene import Scene


class IControl(Protocol):
    config: "Config"
    event: "EventBus"
    screen: "Screen"
    entities: "EntityManager"
    map: "Map"
    deltatime: "float"

    @abstractmethod
    def transition(self, to_scene: "Scene"):
        ...
