from ..icontrol import IControl
from ..menu import StartMenu
from .scene import Scene


class StartScene(Scene):
    def __init__(self, control: IControl, play_scene: str):
        menu = StartMenu(control)

        super().__init__(control, menu, [])

        self.__play_scene = play_scene

    def enter(self):
        self.control.transition(self.__play_scene)

    def update(self):
        ...

    def render(self):
        self.menu.render()
