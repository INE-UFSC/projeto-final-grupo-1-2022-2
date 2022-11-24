from abc import ABC, abstractmethod
from typing import Dict, List

from ..icontrol import IControl
from ..library import Listener
from ..menu import Menu
from ..system import System


class Scene(Listener, ABC):
    def __init__(
        self,
        control: IControl,
        menus: Dict[str, Menu] = None,
        systems: List[System] = None,
    ):
        super().__init__()

        self.__control = control
        self.__menus = menus
        self.__current_menu = None
        self.__systems = [] if systems is None else systems
        self.__next_scene = None

        for system in self.__systems:
            self.subscribe(system)

        for menu in self.__menus.values():
            self.subscribe(menu)

    @property
    def control(self):
        return self.__control

    @property
    def current_menu(self):
        return self.__current_menu

    @property
    def systems(self):
        return self.__systems

    @property
    def menus(self):
        return self.__menus

    @property
    def next_scene(self):
        return self.__next_scene

    @current_menu.setter
    def current_menu(self, menu: Menu):
        self.__current_menu = menu

    @next_scene.setter
    def next_scene(self, scene: "Scene"):
        self.__next_scene = scene

    def enter(self):
        ...

    def leave(self):
        ...

    @abstractmethod
    def update(self):
        ...

    def render(self):
        self.__current_menu.render()
