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
        render = RenderComponent((60, 120), "#ff0000")
        move = MoveComponent(pos, (0, 0, 200))
        slide = SlideComponent()

        collider = CubeCollider(move.pos, (60, 110, 4))
        collision = CollisionComponent(collider)

        super().__init__(render, move, collision, slide)

        self.__is_crouched = False

    def crouch(self):
        print("crouch")
        collider = self.get_component(CollisionComponent)
        collider.shape.size.y /= 3
        self.__is_crouched = True

    def uncrouch(self):
        print("uncrouch")
        collider = self.get_component(CollisionComponent)
        collider.shape.size.y *= 3
        self.__is_crouched = False

    @property
    def is_crouched(self):
        return self.__is_crouched
