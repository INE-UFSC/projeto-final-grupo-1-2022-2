from .component import MenuComponent


class Text(MenuComponent):
    message: str

    def render(self, screen):
        ...
