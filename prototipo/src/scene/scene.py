from abc import ABC, abstractmethod
from typing import Dict, Protocol

from ..entities import GameEntities
from ..event import EventBus
from ..keyboard import Keyboard
from ..leaderboard import Leaderboard
from ..mouse import Mouse


class IControl(Protocol):
    event: EventBus
    keyboard: Keyboard
    mouse: Mouse
    scenes: Dict[str, "Scene"]
    current_scene: "Scene"
    leaderboard: Leaderboard
    entities: GameEntities

    @abstractmethod
    def transition(self, to: "Scene", duration: int = 0):
        ...


class Scene(ABC):
    @abstractmethod
    def enter(self, control: IControl):
        ...

    @abstractmethod
    def leave(self, control: IControl):
        ...

    @abstractmethod
    def update(self, control: IControl):
        ...

    @abstractmethod
    def render(self, control: IControl):
        ...
