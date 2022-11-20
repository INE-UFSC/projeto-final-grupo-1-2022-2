from typing import Tuple, Union

import pygame as pg

from .component import MenuComponent


class Text(MenuComponent):
    __message: str

    def __init__(
        self,
        pos: Union[pg.Vector2, Tuple[int, int]],
        message: str,
        size: int = 24,
        color: Union[pg.Color, str] = "#ffffff",
    ):
        pos = pos if isinstance(pos, pg.Vector2) else pg.Vector2(pos)
        color = color if isinstance(color, pg.Color) else pg.Color(color)

        font = pg.font.SysFont(None, size)
        surface = font.render(message, True, color)

        super().__init__(pos, surface)
