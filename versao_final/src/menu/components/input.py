from typing import Tuple, Union

import pygame as pg

from ...library import Listener
from .button import Button
from .component import MenuComponent
from .text import Text


class InputText(MenuComponent):
    def __init__(
        self,
        label: str = " ",
        word_limit: int = 20,
        color: Union[pg.Color, str] = "#6780BF",
        label_color: Union[pg.Color, str] = "#ffffff",
        size: Union[pg.Vector2, Tuple[int, int]] = [250, 50],
        shade_multiplier: float = 0.5,
        pos: Union[pg.Vector2, Tuple[int, int]] = None,
        key: str = None,
    ):

        size = pg.Vector2(size)
        key = label if key is None else key
        surface = pg.Surface(size)
        surface.fill(color)
        super().__init__(pos, size, surface, key)

        color = pg.Color(color)
        color_tuple = (color.r, color.g, color.b, color.a)
        color_when_pressed = pg.Color(
            [value * shade_multiplier for value in color_tuple]
        )

        self.__label = label
        self.__key = key
        self.__color = color
        self.__color_when_pressed = color_when_pressed
        self.__word_limit = word_limit
        self.__is_pressed = False
        self.__text = Text(label, font_color=label_color, pos=pos)
        if pos is not None:
            self.__left_align_text()

    def emit_event(self):
        """
        emite um evento nomeado pelo atributo `key` do componente e com a
        texto atual no input como argumento
        """

        self.event.emit(self.key, self.label)

    @Listener.on(pg.MOUSEBUTTONDOWN)
    def __toggle_pressed(self, event: pg.event.Event):
        if event.button == pg.BUTTON_LEFT:
            if not self.is_pressed and self.is_inside(event.pos):
                self.surface.fill(self.__color_when_pressed)
                self.__is_pressed = True
            elif self.is_pressed and not self.is_inside(event.pos):
                self.__is_pressed = False
                self.surface.fill(self.__color)
            
            self.dirty = True

    @Listener.on(pg.KEYDOWN)
    def __update_text(self, event: pg.event.Event):
        if self.is_pressed:
            if event.key == pg.K_BACKSPACE:
                if len(self.__label) == 1:
                    self.label = ""

                else:
                    self.label = self.__label[:-1]

            elif (
                not event.unicode.isprintable()
                or len(self.__label) >= self.__word_limit
            ):
                return

            else:
                self.label = self.__label + event.unicode

        self.emit_event()
        self.dirty = True

    def render(self, screen):
        if self.pos is not None and self.dirty:
            screen.blit(self.surface, self.pos)
            if self.__text is not None:
                self.__text.fresh_render(screen)
            
            self.dirty = False

    def __left_align_text(self):
        """
        move o atributo `__text` para o centro do botão
        """
        center_left = pg.Vector2(
            self.pos.x + self.size.x // 2, self.pos.y + self.size.y // 2
        )
        text_size = self.__text.size

        new_pos = (
            center_left.x - text_size.x // 2,
            center_left.y - text_size.y // 2,
        )
        self.__text.pos = new_pos
        self.dirty = True

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

        self.__left_align_text()
        self.dirty = True

    @label.setter
    def label(self, label: str):
        self.__text.set_message(label)
        if self.key == self.__label:
            self.key = label

        self.__label = label
        self.dirty = True

    @is_pressed.setter
    def is_pressed(self, value):
        self.__is_pressed = value
