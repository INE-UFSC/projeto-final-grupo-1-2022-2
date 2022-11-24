from abc import ABC, abstractmethod

from ..icontrol import IControl
from ..library import Listener


class System(Listener, ABC):
    __control: IControl

    def __init__(self, control: IControl):
        super().__init__()

        self.__control = control

    def setup(self):
        ...

    def reset(self):
        ...

    @abstractmethod
    def update(self):
        ...

    @property
    def control(self):
        return self.__control
