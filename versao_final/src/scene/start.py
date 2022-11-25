from ..icontrol import IControl
from ..library import Listener
from ..menu import StartMenu
from .scene import Scene
from ..dao import LeaderboardDAO

class StartScene(Scene):
    def __init__(self, control: IControl):
        menus = {
            "start": StartMenu(control),
        }

        super().__init__(control, menus, [])

    def enter(self):
        self.current_menu = self.menus["start"]
        self.control.screen.display.fill((0, 0, 0))

    def update(self):
        if self.next_scene is not None:
            self.control.transition(self.next_scene)
            self.next_scene = None

    def render(self):
        if self.current_menu is not None:
            self.current_menu.render()

    @Listener.on("Play")
    def __to_main_scene(self):
        self.next_scene = self.control.scene.scenes["main"]

    @Listener.on("Quit")
    def __stop_running(self):
        self.control.stop_running()

    @Listener.on("set player_name")
    def __set_player_name(self, player_name: str):
        self.control.config.player_name = player_name
