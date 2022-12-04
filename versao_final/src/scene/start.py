from ..dao import LeaderboardDAO
from ..icontrol import IControl
from ..library import Listener
from ..menu import LeaderBoardMenu, StartMenu
from .scene import Scene


class StartScene(Scene):
    def __init__(self, control: IControl):
        menus = {
            "start": StartMenu(control),
            "leaderboards": LeaderBoardMenu(control),
        }

        super().__init__(control, menus, [])

    def enter(self):
        self.current_menu = self.menus["start"]
        self.__render_background()
        super().enter()

    def update(self):
        self.current_menu.update()
        if self.next_scene is not None:
            self.control.transition(self.next_scene)
            self.next_scene = None

        if self.next_menu is not None:
            self.current_menu.leave()
            self.__render_background()

            self.current_menu = self.next_menu
            self.next_menu = None

            self.current_menu.enter()
            self.current_menu.fresh_render()

    def render(self):
        if self.current_menu is not None:
            self.current_menu.render()

    @Listener.on("menu fresh_render")
    def __render_background(self):
        self.control.scene.scenes["main"].render_as_background()

    @Listener.on("Play")
    def __to_main_scene(self):
        self.next_scene = self.control.scene.scenes["main"]

    @Listener.on("Return to start menu")
    def __to_start_menu(self):
        self.next_menu = self.menus["start"]

    @Listener.on("Leaderboards")
    def __to_leaderboards(self):
        self.next_menu = self.menus["leaderboards"]

    @Listener.on("Quit")
    def __stop_running(self):
        self.control.stop_running()

    @Listener.on("player_name")
    def __set_player_name(self, name: str):
        if name.strip() == "":
            name = self.control.config.default_player_name
        LeaderboardDAO().set_player_name(name)
