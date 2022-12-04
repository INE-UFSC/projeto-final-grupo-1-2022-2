from ..components import (CollisionComponent, MoveComponent, RenderComponent,
                          SlideComponent)
from ..dao import TextureDAO
from ..library import CubeCollider, class_name
from .entity import Entity


class Player(Entity):
    def __init__(self, pos):
        color = "#ff0000"

        self.__move = MoveComponent(pos, (0, 0, 350))
        self.__slide = SlideComponent()

        collider_uncrouched = CubeCollider(self.__move.pos, (60, 110, 4))
        collider_crouched = CubeCollider(self.__move.pos, (60, 55, 4))

        self.__collision = {
            "crouched": CollisionComponent(collider_crouched),
            "uncrouched": CollisionComponent(collider_uncrouched),
        }

        texture_path = f"{class_name(self)}.png"
        surface = TextureDAO().load(texture_path, lambda: collider_uncrouched.get_surface(color))

        self.__render = RenderComponent(surface)

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
