from typing import Tuple, Union

import pygame as pg

from .component import MenuComponent


class Text(MenuComponent):
    __message: str
    __color: pg.Color
    __font: pg.font.Font

    def __init__(
        self,
        message: str,
        font_size: int = 24,
        font_color: Union[pg.Color, str] = "#ffffff",
        font_name: Union[str, None] = "Helvetica",
        pos: Union[pg.Vector2, Tuple[int, int]] = None,
        key: str = None,
    ):
        key = message if key is None else key

        self.__color = pg.Color(font_color)
        self.__message = message

        self.__font = pg.font.SysFont(font_name, font_size)
        surface = self.__font.render(self.__message, True, self.__color)

        super().__init__(pos, surface.get_size(), surface, key)

    @property
    def message(self):
        return self.__message

    @property
    def color(self):
        return self.__color

    def set_message(self, message: str):
        if self.key == self.__message:
            self.__key = message

        self.surface = self.__font.render(message, True, self.__color)
        self.__message = message
