import pygame as pg

from ..components import MoveComponent, RenderComponent
from ..icontrol import IControl
from .system import System


class RenderSystem(System):
    __show_origin: bool = True

    def update(self):
        ctl = self.control
        screen = ctl.screen

        entities = ctl.entities.get_all_with(RenderComponent, MoveComponent)

        screen.display.fill("#0bf502")

        for entity in entities:
            render = entity.get_component(RenderComponent)
            move = entity.get_component(MoveComponent)

            origin = screen.get_pos(move.pos)
            dest_pos = (origin[0] - render.origin[0], origin[1] - render.origin[1])

            screen.display.blit(render.surface, dest_pos)

            if self.__show_origin:  # DEBUG
                pg.draw.circle(screen.display, "#ffffff", origin, 3)