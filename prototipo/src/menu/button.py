from typing import Callable

from .component import MenuComponent


class Button(MenuComponent):
    label: str
    is_pressed: bool
    is_hovered: bool
    action: Callable

    def hover(self):
        ...

    def unhover(self):
        ...

    def press(self):
        ...

    def release(self):
        ...

    def render(self, screen):
        ...
