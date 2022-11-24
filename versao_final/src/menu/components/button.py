from typing import Callable, List, Tuple, Union

import pygame as pg

from ...library import Listener
from .component import MenuComponent
from .text import Text


class Button(MenuComponent):
    __label: str
    __color: pg.Color
    __color_when_pressed: pg.Color
    __is_pressed: bool
    __is_hovered: bool
    __key: Union[str, None]

    def __init__(
        self,
        label: str,
        color: Union[pg.Color, str] = "#6780BF",
        color_when_pressed: Union[pg.Color, str] = "#FFA500",
        label_color: Union[pg.Color, str] = "#ffffff",
        size: Union[pg.Vector2, Tuple[int, int]] = (250, 50),
        shade_multiplier: float = 0.5,
        pos: Union[pg.Vector2, Tuple[int, int]] = None,
        key: str = None,
    ):
        key = label if key is None else key

        color = pg.Color(color)
        color_when_pressed = pg.Color(color_when_pressed)
        size = pg.Vector2(size)

        surface = pg.Surface(size)
        surface.fill(color)
        super().__init__(pos, size, surface, key)

        self.__label = label
        self.__key = key
        self.__color = color
        self.__color_when_pressed = color_when_pressed
        self.__shade_multiplier = shade_multiplier

        self.__is_hovered = False
        self.__is_pressed = False

        self.__text = Text(label, font_color=label_color, pos=pos)
        if pos is not None:
            self.__center_text()

    @Listener.on(pg.MOUSEMOTION)
    def hover(self, event: pg.event.Event):
        if not self.is_pressed and self.is_inside(event.pos):
            self.surface.fill(self.color_shaded)
            self.__is_hovered = True

    @Listener.on(pg.MOUSEMOTION)
    def unhover(self, event: pg.event.Event):
        if self.is_hovered:
            if not self.is_inside(event.pos):
                self.surface.fill(self.__color)
                self.__is_hovered = False

    @Listener.on(pg.MOUSEBUTTONDOWN)
    def press(self, event: pg.event.Event):
        if event.button == pg.BUTTON_LEFT and self.is_inside(event.pos):
            self.surface.fill(self.__color_when_pressed)
            self.__is_hovered = False
            self.__is_pressed = True

    @Listener.on(pg.MOUSEBUTTONUP)
    def release(self, event: pg.event.Event):
        if event.button == pg.BUTTON_LEFT and self.is_pressed:
            self.surface.fill(self.__color)
            self.__is_pressed = False
            self.event.emit(self.key)

    def render(self, screen):
        if self.pos is not None:
            screen.blit(self.surface, self.pos)
            if self.__text is not None:
                self.__text.render(screen)

    def __center_text(self):
        """
        move o atributo `__text` para o centro do botão
        """
        button_center = pg.Vector2(
            self.pos.x + self.size.x // 2, self.pos.y + self.size.y // 2
        )
        text_size = self.__text.size

        new_pos = (
            button_center.x - text_size.x // 2,
            button_center.y - text_size.y // 2,
        )
        self.__text.pos = new_pos

    @property
    def color_shaded(self) -> pg.Color:
        color_tuple = (self.__color.r, self.__color.g, self.__color.b, self.__color.a)
        color_shaded = [value * self.__shade_multiplier for value in color_tuple]
        return pg.Color(color_shaded)

    @property
    def is_pressed(self):
        return self.__is_pressed

    @property
    def is_hovered(self):
        return self.__is_hovered

    @property
    def label(self):
        return self.__label

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pg.Vector2(pos)
        self.__text.pos = pg.Vector2(pos)

        self.__center_text()

    @label.setter
    def label(self, label: str):
        self.__text.message = label
        if self.key == self.__label:
            self.key = label

        self.__label = label
