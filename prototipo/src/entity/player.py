from ..components import (
    CollisionComponent,
    MoveComponent,
    RenderComponent,
    SlideComponent,
)
from ..library import CubeCollider
from .entity import Entity


class Player(Entity):
    def __init__(self, pos):
        render = RenderComponent((100, 200), "#ff0000")
        move = MoveComponent(pos, (0, 0, 200))
        slide = SlideComponent()

        collider = CubeCollider(move.pos, (100, 200, 1))
        collision = CollisionComponent(collider)

        super().__init__(render, move, collision, slide)
