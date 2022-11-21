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
        self.__render = RenderComponent((60, 120), "#ff0000")
        self.__move = MoveComponent(pos, (0, 0, 200))
        self.__slide = SlideComponent()

        self.__collider = CubeCollider(self.__move.pos, (60, 110, 4))
        self.__collision = CollisionComponent(self.__collider)

        super().__init__(self.__render, self.__move, self.__collision, self.__slide)

        self.__is_crouched = False

    def crouch(self):
        collider = self.get_component(CollisionComponent)
        collider.shape.size.y /= 3
        self.__is_crouched = True

    def uncrouch(self):
        collider = self.get_component(CollisionComponent)
        collider.shape.size.y *= 3
        self.__is_crouched = False

    @property
    def is_crouched(self):
        return self.__is_crouched
