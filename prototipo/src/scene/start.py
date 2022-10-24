from .scene import IControl, Scene


class StartScene(Scene):
    def __init__(self, control: IControl, play_scene: str):
        menu = None

        super().__init__(control, menu, [])

        self.__play_scene = play_scene

    def enter(self):
        self.control.transition(self.__play_scene)

    def update(self):
        ...
