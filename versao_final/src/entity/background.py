from typing import Callable, Tuple, Union
import pygame as pg

from ..components import (
    PosComponent,
    RenderComponent,
)
from ..dao import TextureDAO
from .entity import Entity


class Background(Entity):
    def __init__(
        self,
        pos: Tuple[int, int, int] = (0, -1, 0),
        default_surface: Union[pg.Surface, Callable[..., pg.Surface]] = None
    ):
        pos = PosComponent(pos)

        # size = surface.get_size()
        # origin = (size[0] // 2.78, size[1] // 1.093)

        surface = TextureDAO().load("background/default.png", default_surface)
        render = RenderComponent(surface)

        super().__init__(pos, render)
