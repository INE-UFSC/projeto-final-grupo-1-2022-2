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

        collider_uncrouched = CubeCollider(self.__move.pos, (60, 110, 4))
        collider_crouched = CubeCollider(self.__move.pos, (60, 55, 4))

        self.__collision = {
            "crouched": CollisionComponent(collider_crouched),
            "uncrouched": CollisionComponent(collider_uncrouched),
        }

        super().__init__(
            self.__render, self.__move, self.__collision["uncrouched"], self.__slide
        )

        self.__is_crouched = False

    def crouch(self):

        self.set_component(CollisionComponent, self.__collision["crouched"])
        self.__is_crouched = True

    def uncrouch(self):
        self.set_component(CollisionComponent, self.__collision["uncrouched"])
        self.__is_crouched = False

    @property
    def is_crouched(self):
        return self.__is_crouched
