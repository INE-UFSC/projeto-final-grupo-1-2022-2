from abc import ABC, abstractmethod

from pygame import Vector2


class MenuComponent(ABC):
    pos: Vector2

    @abstractmethod
    def render(self):
        ...
