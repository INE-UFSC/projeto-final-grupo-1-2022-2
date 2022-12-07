from abc import ABC, abstractmethod
from typing import List, Tuple, Union

import pygame as pg

from ..library import Screen
from .components import MenuComponent
from time import time

class Render(ABC):
    """
    classe base para a renderização do menu
    """

    _components: List[MenuComponent]
    def __init__(self, components: List[List[MenuComponent]]):
        self._components = []
        for listt in components:
            self._components.extend(listt)


    @abstractmethod
    def render(self):
        ...
    
    @abstractmethod
    def fresh_render(self):
        ...

    def setup(self):
        ...
    
    def reset(self):
        ...
    
    



class DefaultRender(Render):
    """
    renderiza menus sem transparência ou cor de fundo
    """

    __screen: Screen

    def __init__(self, screen: Screen, components: List[List[MenuComponent]]) -> None:
        super().__init__(components)
        self.__screen = screen

    def render(self):
        for component in self._components:
            component.render(self.__screen.display)

    def fresh_render(self):
        for component in self._components:
            component.fresh_render(self.__screen.display)


class BackgroundRender(Render):
    """
    renderiza menus sem transparência na tela inteira, mas com cor de fundo
    """

    __screen: Screen
    __bg: pg.Surface  # background
    __bg_color: pg.Color
    __pos: pg.Vector2
    __size: pg.Vector2
    __fade: bool
    __rendered: bool = False
    __fade_duration: float
    __fade_start: float

    def __init__(
        self,
        screen: Screen,
        components: List[List[MenuComponent]],
        background_color: Union[pg.Color, str],
        menu_pos: pg.Vector2,
        menu_size: pg.Vector2,
        fade: bool = False,
        fade_duration: float = 0.5
    ) -> None:
        super().__init__(components)
        self.__screen = screen
        self.__bg = pg.Surface(menu_size, pg.SRCALPHA)
        self.__bg_color = pg.Color(background_color)
        self.__pos = menu_pos
        self.__size = menu_size
        self.__fade = fade
        self.__fade_duration = fade_duration
        self.__fade_start = 0


    def render(self):
        screen = self.__screen.display
        bg = self.__bg

        render_with_fade = self.__fade and time() - self.__fade_start < self.__fade_duration
        render_once_without_fade = not self.__fade and not self.__rendered

        if render_with_fade or render_once_without_fade:
            bg.fill(self.__bg_color)
            screen.blit(bg, self.__pos)

        for component in self._components:
            if render_with_fade or render_once_without_fade:
                component.fresh_render(screen)
            else:
                component.render(screen)

        self.__rendered = True

    def fresh_render(self):
        self.__rendered = False
        self.render()

    def reset(self):
        self.__rendered = False
        self.__fade_start = 0

    def setup(self):
        self.__fade_start = time()



class TransparencyBackgroundRender(Render):
    """
    renderiza menu com cor de fundo e transparência
    """

    __screen: Screen
    __bg: pg.Surface  # background
    __bg_color: pg.Color
    __transparent_layer: pg.Surface
    __transparent_color: pg.Color
    __transparent_layer_fade: bool
    __pos: pg.Vector2
    __size: pg.Vector2
    __rendered: bool = False
    __fade_duration: float
    __fade_start: float

    def __init__(
        self,
        screen: Screen,
        components: List[List[MenuComponent]],
        background_color: Union[pg.Color, str],
        menu_pos: pg.Vector2,
        menu_size: pg.Vector2,
        transparency_color: Union[pg.Color, Tuple[int, int, int, int]],
        transparency_layer_fade: bool = False,
        fade_duration: int = 0.6
    ) -> None:
        super().__init__(components)
        self.__screen = screen
        self.__bg = pg.Surface(menu_size)
        self.__bg_color = pg.Color(background_color)
        self.__transparent_layer = pg.Surface(screen.size, pg.SRCALPHA)
        self.__transparent_color = pg.Color(transparency_color)
        self.__transparent_layer_fade = transparency_layer_fade
        self.__pos = menu_pos
        self.__size = menu_size
        self.__fade_duration = fade_duration
        self.__fade_start = 0
        

    def render(self):
        render_with_fade = self.__transparent_layer_fade and time() - self.__fade_start < self.__fade_duration
        render_once_without_fade = not self.__transparent_layer_fade and not self.__rendered
        
        if render_with_fade or render_once_without_fade:   
            # renderiza apenas uma vez caso não haja fade ou várias se houver
            self.__transparent_layer.fill(self.__transparent_color)
            self.__bg.fill(self.__bg_color)
            self.__transparent_layer.blit(self.__bg, self.__pos)
            self.__screen.display.blit(self.__transparent_layer, (0, 0))


        for component in self._components:
            if render_with_fade or render_once_without_fade:
                component.fresh_render(self.__screen.display)
            else:
                component.render(self.__screen.display)
        
        self.__rendered = True

    def fresh_render(self):
        self.__rendered = False
        self.render()

    def reset(self):
        self.__rendered = False
        self.__fade_start = 0

    def setup(self):
        self.__fade_start = time()