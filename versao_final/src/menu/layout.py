from abc import ABC, abstractmethod
from functools import reduce
from typing import Dict, List

import pygame as pg

from .components import MenuComponent

# TODO
# arrumar os cálculos do GridLayout


class Layout(ABC):
    def __init__(
        self,
        components: List[List[MenuComponent]],
        surface_size: pg.Vector2,
        spacing: pg.Vector2 = pg.Vector2(50, 100),
        padding: pg.Vector2 = pg.Vector2(50, 50),
        center_x: bool = False,
        center_y: bool = False,
    ) -> None:
        """
        Layout utilizado para posicionar os componentes na tela

        parâmetros:
        - `components`: Matriz com os componentes que serão utilizados no menu. Cada linha da matriz corresponde à uma linha do menu;
        - `surface_size`: tamanho da surface na qual o menu será renderizado. Na prática, sempre será a tela do jogo;
        - `spacing`: espaçamento entre os componentes;
        - `padding`: distancia entre os componentes e a borda da tela;
        - `center_x`: centralizar o eixo x do menu na tela;
        - `center_y`: centralizar o eixo y do menu na tela
        """
        ...

    @abstractmethod
    def center_x(self):
        """centraliza os componentes do layout no eixo x"""
        ...

    @abstractmethod
    def center_y(self):
        """centraliza os componentes do layout no eixo y"""
        ...

    @abstractmethod
    def get_all_components(self) -> List[MenuComponent]:
        ...

    @abstractmethod
    def get_component(self, key: str) -> MenuComponent:
        ...

    @abstractmethod
    def get_size(self) -> pg.Vector2:
        ...

    @abstractmethod
    def get_pos(self) -> pg.Vector2:
        ...


class GridLayout(Layout):
    __padding: pg.Vector2
    __spacing: pg.Vector2
    __surface_size: pg.Vector2
    __lines: List["GridLine"]

    def __init__(
        self,
        components: List[List[MenuComponent]],
        surface_size: pg.Vector2,
        spacing: pg.Vector2 = pg.Vector2(50, 100),
        padding: pg.Vector2 = pg.Vector2(50, 50),
        center_x: bool = False,
        center_y: bool = False,
    ) -> None:
        """
        Layout grid utilizado para posicionar os componentes na tela

        parâmetros:
        - `components`: Matriz com os componentes que serão utilizados no menu. Cada linha da matriz corresponde à uma linha do menu;
        - `surface_size`: tamanho da surface na qual o menu será renderizado.
        - `spacing`: espaçamento entre os componentes;
        - `padding`: distancia entre os componentes e a borda da tela;
        - `center_x`: centralizar o eixo x do menu na tela;
        - `center_y`: centralizar o eixo y do menu na tela
        """

        self.__lines = []
        for line in components:
            self.__lines.append(GridLine(line, spacing))

        self.__spacing = spacing
        self.__padding = padding
        self.__surface_size = pg.Vector2(surface_size)

        self.__create_grid_layout()
        if center_x:
            self.center_x()
        if center_y:
            self.center_y()

    def __create_grid_layout(self) -> None:
        """
        cria um grid com os `components` por meio da
        alteração da posição destes
        """
        for i, line in enumerate(self.__lines):
            y_pos = self.__padding.y + i * self.__spacing.y
            for j, component in enumerate(line.components.values()):
                x_pos = self.__padding.x + j * self.__spacing.x
                component.pos = (x_pos, y_pos)

    def center_x(self):
        """
        centraliza os componentes no eixo x
        """
        for line in self.__lines:
            prev_x_pos = 0
            left_boundary = self.__surface_size.x // 2 - line.size.x // 2
            for component in line.components.values():
                component.pos = (
                    left_boundary + self.__spacing.x + prev_x_pos,
                    component.pos.y,
                )
                prev_x_pos = component.pos.x + component.size.x - left_boundary

    def center_y(self):
        """
        centraliza os componentes no eixo y
        """
        line_y_sizes = [line.size.y for line in self.__lines]
        y_size = reduce(lambda x, y: x + y, line_y_sizes) - self.__spacing.y // 2

        top_boundary = self.__surface_size.y // 2 - y_size // 2
        prev_y_pos = 0
        for i, line in enumerate(self.__lines):
            line_y_pos = 0
            for component in line.components.values():
                if i > 0:
                    component.pos = (
                        component.pos.x,
                        top_boundary + self.__spacing.y + prev_y_pos,
                    )
                else:
                    component.pos = (component.pos.x, top_boundary + prev_y_pos)
                line_y_pos = component.pos.y - top_boundary

            prev_y_pos = line_y_pos

    def get_all_components(self) -> List[MenuComponent]:
        components = []
        for line in self.__lines:
            for component in line.components.values():
                components.append(component)
        return components

    def get_component(self, key: str):
        for line in self.__lines:
            if key in line.components.keys():
                return line.components.get(key)

    def get_size(self):
        size = pg.Vector2(0, 0)

        for line in self.__lines:
            size.x = max(line.size.x, size.x)
            size.y += line.size.y

        size += self.__padding
        size.y += self.__padding.y // 2
        return size

    def get_pos(self):
        leftmost_line = min(self.__lines, key=lambda x: x.pos.x)
        heighest_line = min(self.__lines, key=lambda x: x.pos.y)

        pos = pg.Vector2(leftmost_line.pos.x, heighest_line.pos.y)

        return pos - self.__padding


class GridLine:
    __components: Dict[str, MenuComponent]
    __spacing: pg.Vector2
    __size: pg.Vector2

    def __init__(self, components: List[MenuComponent], spacing: pg.Vector2) -> None:
        self.__components = {component.key: component for component in components}
        self.__spacing = spacing
        self.__size = self.__calculate_size()

    def __calculate_size(self):
        x_size = 0
        for component in self.__components.values():
            x_size += component.size.x + self.__spacing.x

        return pg.Vector2(x_size, self.__spacing.y)

    @property
    def pos(self):
        top_left = min(self.__components.values(), key=lambda a: a.pos.x)
        return top_left.pos

    @property
    def size(self):
        return self.__size

    @property
    def components(self):
        return self.__components
