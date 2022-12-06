from functools import cmp_to_key

import pygame as pg

from ..components import CollisionComponent, PosComponent, RenderComponent
from ..entity import Entity
from .system import System
from ..library import class_name


def compare_pos(a: Entity, b: Entity) -> int:
    collision_a = a.get_component(CollisionComponent)
    collision_b = b.get_component(CollisionComponent)

    if collision_a and collision_b:
        A = collision_a.shape
        B = collision_b.shape

        if A.y_max <= B.y_min:
            return -1
        if B.y_max <= A.y_min:
            return 1

        return B.z_max - A.z_max

    pos_a = a.get_component(PosComponent)
    pos_b = b.get_component(PosComponent)

    return pos_a.value.y - pos_b.value.y


class RenderSystem(System):
    __show_origin: bool = False

    def update(self):
        ctl = self.control
        screen = ctl.screen

        entities = ctl.entities.get_all_with(RenderComponent, PosComponent)
        entities = sorted(entities, key=cmp_to_key(compare_pos))

        screen.display.fill(pg.Color("#0bf502"))

        for entity in entities:
            render = entity.get_component(RenderComponent)
            pos = entity.get_component(PosComponent)

            origin = screen.get_pos(pos.value)
            dest_pos = (origin[0] - render.origin[0], origin[1] - render.origin[1])

            screen.display.blit(render.surface, dest_pos)

            if self.__show_origin:  # DEBUG
                pg.draw.circle(screen.display, pg.Color("#ffffff"), origin, 3)
