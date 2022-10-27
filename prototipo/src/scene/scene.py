from abc import ABC, abstractmethod
from typing import Dict, List, Protocol

from ..entity import EntityManager
from ..leaderboard import Leaderboard
from ..library import EventBus, Keyboard, Listener, Mouse
from ..menu import Menu
from ..system import System


class IControl(Protocol):
    event: EventBus
    keyboard: Keyboard
    mouse: Mouse
    leaderboard: Leaderboard
    entities: EntityManager
    deltatime: float

    @abstractmethod
    def transition(self, to_scene: "Scene"):
        ...


class Scene(Listener, ABC):
    def __init__(
        self, control: IControl, menu: Menu = None, systems: List[System] = None
    ):
        super().__init__()

        self.__control = control
        self.__menu = menu
        self.__systems = [] if systems is None else systems

        for system in self.__systems:
            self.subscribe(system)

    @property
    def control(self):
        return self.__control

    @property
    def menu(self):
        return self.__menu

    @property
    def systems(self):
        return self.__systems

    def enter(self):
        ...

    def leave(self):
        ...

    @abstractmethod
    def update(self):
        ...

    def render(self):
        ...
