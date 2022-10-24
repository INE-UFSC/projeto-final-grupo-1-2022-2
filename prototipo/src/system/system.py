from abc import ABC, abstractmethod

from ..entity import EntityManager
from ..library import Listener


class System(Listener, ABC):
    def __init__(self, entities: EntityManager):
        super().__init__()

        self.__entities = entities

    @property
    def entities(self):
        return self.__entities

    @abstractmethod
    def update(self):
        ...
