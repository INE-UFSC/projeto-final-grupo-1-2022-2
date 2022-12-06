from typing import Tuple

from ..components import (
    MoveComponent,
    RenderComponent,
)
from ..dao import TextureDAO
from .entity import Entity


class Background(Entity):
    def __init__(self, pos: Tuple[int, int, int] = (0, -1, 0)):
        surface = TextureDAO().load("teste.png")
        move = MoveComponent(pos, (0, 0, 0))

        # size = surface.get_size()
        # origin = (size[0] // 2.78, size[1] // 1.093)

        render = RenderComponent(surface)

        super().__init__(move, render)
