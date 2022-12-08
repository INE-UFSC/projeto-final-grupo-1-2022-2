from abc import ABC, abstractmethod
from typing import Tuple, List,Dict
from functools import reduce

import pygame as pg

from .components import MenuComponent



class Layout(ABC):
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
        spacing: pg.Vector2 = pg.Vector2(50, 25),
        padding: pg.Vector2 = pg.Vector2(50, 50),
        center_x: bool = False,
        center_y: bool = False,
        pos: Tuple[int,int] = None
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
        - `pos`: posição do ponto mais alto e à esquerda do menu
        """

        self.__spacing = pg.Vector2(spacing)
        self.__padding = pg.Vector2(padding)
        self.__surface_size = pg.Vector2(surface_size)

        self.__lines = []
        for line in components:
            self.__lines.append(GridLine(line, self.__spacing))

        if pos is None:
            x_boundary = surface_size[0] // 2 if center_x else padding[0]
            y_boundary = surface_size[1] // 2 - (self.get_size().y - self.__padding.y*2) // 2 if center_y else padding[1]
        else:
            size = self.get_size()
            x_boundary = pos[0] + size.x // 2 if center_x else pos[0] + padding[0]
            y_boundary = surface_size[1] // 2 - (size.y - padding[1]*2) // 2 if center_y and pos[1] == None else  pos[1] + padding[1]

        self.__create_grid_layout(x_boundary, y_boundary, center_x, center_y)

    def __create_grid_layout(self, x_boundary: float, y_boundary: float, center_x: bool, center_y: bool) -> None:
        """
        cria um grid com os `components` por meio da
        alteração da posição destes
        """
        
        prev_y_pos = 0
        top_boundary = y_boundary
        for line in self.__lines:
            line_y_pos = 0 # posição do ponto mais baixpo do maior elemento da linha anterior + espaçamento
            prev_x_pos = 0  # posição do ponto mais a direita do elemento anterior da linha + espaçamento

            left_boundary = x_boundary
            if center_x:
                left_boundary = x_boundary - line.size.x // 2

            for component in line.components.values():
                if component.pos is None:
                    component.pos = (
                        left_boundary + prev_x_pos, top_boundary + prev_y_pos
                    )

                prev_x_pos = component.pos.x + self.__spacing.x + component.size.x + component.spacing.x - left_boundary
                line_y_pos = max(component.pos.y + self.__spacing.y + component.size.y + component.spacing.y - top_boundary, line_y_pos)
            
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
            size.y += line.size.y + self.__spacing.y

        size += self.__padding + self.__padding
        size.y -= self.__spacing.y
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
        y_size = 0
        for component in self.__components.values():
            x_size += component.size.x + self.__spacing.x + component.spacing.x
            y_size = max(y_size, component.size.y + component.spacing.y)

        x_size -= self.__spacing.x
        return pg.Vector2(x_size, y_size)

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
