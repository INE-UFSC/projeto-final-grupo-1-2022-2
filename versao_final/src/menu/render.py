from abc import ABC, abstractmethod
from typing import List, Tuple, Union

import pygame as pg

from ..library import Screen
from .components import MenuComponent


class Render(ABC):
    """
    classe base para a renderização do menu
    """

    @abstractmethod
    def render(self):
        ...


class DefaultRender(Render):
    """
    renderiza menus sem transparência ou cor de fundo
    """

    __screen: Screen
    __components: List[MenuComponent]

    def __init__(self, screen: Screen, components: List[MenuComponent]) -> None:
        self.__components = components
        self.__screen = screen

    def render(self):
        for component in self.__components:
            component.render(self.__screen.display)


class BackgroundRender(Render):
    """
    renderiza menus sem transparência, mas com cor de fundo
    """

    __screen: Screen
    __components: List[MenuComponent]
    __bg: pg.Surface  # background
    __bg_color: pg.Color
    __pos: pg.Vector2
    __size: pg.Vector2

    def __init__(
        self,
        screen: Screen,
        components: List[MenuComponent],
        background_color: Union[pg.Color, str],
        menu_pos: pg.Vector2,
        menu_size: pg.Vector2,
    ) -> None:
        self.__screen = screen
        self.__components = components
        self.__bg = pg.Surface(menu_size)
        self.__bg_color = pg.Color(background_color)
        self.__pos = menu_pos
        self.__size = menu_size

    def render(self):
        screen = self.__screen.display
        bg = self.__bg
        bg.fill(self.__bg_color)

        screen.blit(bg, self.__pos)

        for component in self.__components:
            component.render(screen)


class TransparencyRender(Render):
    """
    renderiza menus com fundo transparente
    """

    __screen: Screen
    __components: List[MenuComponent]
    __transparent_layer: pg.Surface
    __transparent_color: pg.Color

    def __init__(
        self,
        screen: Screen,
        components: List[MenuComponent],
        transparency_color: Union[pg.Color, Tuple[int, int, int, int]],
    ):
        self.__screen = screen
        self.__components = components
        self.__transparent_layer = pg.Surface(screen.size, pg.SRCALPHA)
        self.__transparent_color = pg.Color(transparency_color)

    def render(self):
        self.__transparent_layer.fill(self.__transparent_color)

        for component in self.__components:
            component.render(self.__transparent_layer)

        self.__screen.display.blit(self.__transparent_layer, (0, 0))


class TransparencyBackgroundRender(Render):
    """
    renderiza menu com cor de fundo e transparência
    """

    __screen: Screen
    __components: List[MenuComponent]
    __bg: pg.Surface  # background
    __bg_color: pg.Color
    __transparent_layer: pg.Surface
    __transparent_color: pg.Color
    __pos: pg.Vector2
    __size: pg.Vector2

    def __init__(
        self,
        screen: Screen,
        components: List[MenuComponent],
        background_color: Union[pg.Color, str],
        menu_pos: pg.Vector2,
        menu_size: pg.Vector2,
        transparency_color: Union[pg.Color, Tuple[int, int, int, int]],
    ) -> None:
        self.__screen = screen
        self.__components = components
        self.__bg = pg.Surface(menu_size)
        self.__bg_color = pg.Color(background_color)
        self.__transparent_layer = pg.Surface(screen.size, pg.SRCALPHA)
        self.__transparent_color = pg.Color(transparency_color)
        self.__pos = menu_pos
        self.__size = menu_size

    def render(self):
        self.__transparent_layer.fill(self.__transparent_color)
        self.__bg.fill(self.__bg_color)
        self.__transparent_layer.blit(self.__bg, self.__pos)

        for component in self.__components:
            component.render(self.__transparent_layer)
        self.__screen.display.blit(self.__transparent_layer, (0, 0))
