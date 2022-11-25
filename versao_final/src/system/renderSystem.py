from functools import cmp_to_key

import pygame as pg

from ..components import CollisionComponent, MoveComponent, RenderComponent
from ..entity import Entity
from .system import System


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


class RenderSystem(System):
    __show_origin: bool = False

    def update(self):
        ctl = self.control
        screen = ctl.screen

        entities = ctl.entities.get_all_with(RenderComponent, MoveComponent)
        entities = sorted(entities, key=cmp_to_key(compare_pos))

        screen.display.fill(pg.Color("#0bf502"))

        for entity in entities:
            render = entity.get_component(RenderComponent)
            move = entity.get_component(MoveComponent)

            origin = screen.get_pos(move.pos)
            dest_pos = (origin[0] - render.origin[0], origin[1] - render.origin[1])

            screen.display.blit(render.surface, dest_pos)

            if self.__show_origin:  # DEBUG
                pg.draw.circle(screen.display, pg.Color("#ffffff"), origin, 3)