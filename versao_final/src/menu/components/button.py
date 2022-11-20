from typing import Callable, List, Tuple, Union

import pygame as pg

from ...library import Listener
from .component import MenuComponent
from .text import Text


class Button(MenuComponent):
    __label: str
    __is_pressed: bool
    __is_hovered: bool
    __on_click: Callable
    __color: pg.Color
    __color_when_pressed: pg.Color
    __shade_multiplier: float

    def __init__(
        self,
        pos: Union[pg.Vector2, Tuple[int, int]],
        on_click: Callable,
        label: str,
        color: Union[pg.Color, str] = "#6780BF",
        color_when_pressed: Union[pg.Color, str] = "#FFA500",
        label_color: Union[pg.Color, str] = "#ffffff",
        size: Union[pg.Vector2, Tuple[int, int]] = (100, 100),
        shade_multiplier: float = 0.5,
        press_duration: int = 300,
    ):
        pos = pg.Vector2(pos)
        size = pg.Vector2(size)
        color = pg.Color(color)
        label_color = pg.Color(label_color)

        surface = pg.Surface(size)
        surface.fill(color)

        self.__text = Text(pos, label, color=label_color)
        self.__color = color
        self.__color_when_pressed = color_when_pressed
        self.__shade_multiplier = shade_multiplier
        self.__press_duration = press_duration
        super().__init__(pos, surface)

    @Listener.on(pg.MOUSEMOTION)
    def hover(self, event: pg.event.Event):
        if not self.is_pressed and self.is_inside(event.pos):
            color = self.__color
            color_shaded = color * self.__shade_multiplier
            self.__surface.fill(color_shaded)

    @Listener.on(pg.MOUSEMOTION)
    def unhover(self, event: pg.event.Event):
        if self.is_hovered:
            if not self.is_inside(event.pos):
                self.__surface.fill(self.__color)

    @Listener.on(pg.MOUSEBUTTONDOWN)
    def press(self, event: pg.event.Event):
        if event.button == pg.BUTTON_LEFT and self.is_inside(event.pos):
            self.__surface.fill(self.__color_when_pressed)
            self.__action()

    @Listener.on(pg.MOUSEBUTTONUP)
    def release(self, event: pg.event.Event):
        if event.button == pg.BUTTON_LEFT and self.is_pressed:
            self.__surface.fill(self.__color)

    def render(self, screen):
        screen.blit(self.__surface, self.__pos)
        self.__text.render(screen)

    def is_inside(self, coordinate: Union[pg.Vector2, Tuple[int, int]]) -> bool:
        x_min = self.__pos.x
        x_max = self.__pos.x + self.__surface.get_width()
        y_min = self.__pos.y
        y_max = self.__pos.y + self.__surface.get_height()
        coordinate = pg.Vector2(coordinate)

        return x_min < coordinate.x < x_max and y_min < coordinate.y < y_max

    @property
    def current_color(self):
        button_pos = self.__surface.get_rect().center()
        color = self.__surface.get_at(button_pos)
        return color

    @property
    def is_hovered(self):
        return self.current_color == self.__color * self.__shade_multiplier

    @property
    def is_pressed(self):
        return self.current_color == self.__color_when_pressed
