from typing import Tuple

from ..components import (
    PosComponent,
    RenderComponent,
)
from ..dao import TextureDAO
from .entity import Entity


class Background(Entity):
    def __init__(self, pos: Tuple[int, int, int] = (0, -1, 0)):
        pos = PosComponent(pos)

        # size = surface.get_size()
        # origin = (size[0] // 2.78, size[1] // 1.093)

        surface = TextureDAO().load("teste.png")
        render = RenderComponent(surface)

        super().__init__(pos, render)
