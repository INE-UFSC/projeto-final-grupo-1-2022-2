from typing import Callable, Tuple, List, Union
from random import randint
import pygame as pg

from ..components import (
    PosComponent,
    RenderComponent,
)
from ..dao import TextureDAO
from .entity import Entity


class Background(Entity):
    __textures: List[pg.Surface] = TextureDAO().load_many("background")

    def __init__(
        self,
        pos: Tuple[int, int, int] = (0, -1, 0),
        default_surface: Union[pg.Surface, Callable[..., pg.Surface]] = None
    ):
        pos = PosComponent(pos)

        if self.__textures:
            i = randint(0, len(self.__textures) - 1)
            surface = self.__textures[i]
        else:
            surface = TextureDAO().load("background/default.png", default_surface)

        render = RenderComponent(surface)

        super().__init__(pos, render)
