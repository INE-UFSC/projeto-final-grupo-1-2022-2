from ..icontrol import IControl
from ..library import Listener
from ..menu import StartMenu
from .scene import Scene


class StartScene(Scene):
    def __init__(self, control: IControl, play_scene: str):
        menus = {
            "start": StartMenu(control),
        }

        super().__init__(control, menus, [])

        self.__play_scene = play_scene

    def enter(self):
        self.current_menu = self.menus["start"]
        ...

    def update(self):
        ...

    def render(self):
        if self.current_menu is not None:
            self.current_menu.render()

    @Listener.on("Play")
    def leave(self):
        self.control.transition(self.__play_scene)

    @Listener.on("Quit")
    def __stop_running(self):
        self.control.stop_running()
