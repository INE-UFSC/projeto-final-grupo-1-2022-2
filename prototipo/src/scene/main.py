from .scene import IControl, Scene


class MainScene(Scene):
    def __init__(self, control: IControl):
        menu = None
        systems = []

        super().__init__(control, menu, systems)

    def update(self):
        ...
