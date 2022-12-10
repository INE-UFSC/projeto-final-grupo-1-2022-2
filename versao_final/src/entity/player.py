from ..components import (
    CollisionComponent,
    PosComponent,
    MoveComponent,
    RenderComponent,
    SlideComponent,
)
from ..dao import TextureDAO
from ..library import CubeCollider
from .entity import Entity


class Player(Entity):
    def __init__(self, pos):
        color = "#ff0000"

        pos_comp = PosComponent(pos)
        self.__move = MoveComponent((0, 0, 350))
        self.__slide = SlideComponent()

        collider_uncrouched = CubeCollider(pos_comp.value, (60, 110, 4))
        collider_crouched = CubeCollider(pos_comp.value, (60, 55, 4))

        self.__collision = {
            "crouched": CollisionComponent(collider_crouched),
            "uncrouched": CollisionComponent(collider_uncrouched),
        }

        txt_dao = TextureDAO()
        render = RenderComponent(
            alpha=True,
            default=txt_dao.load(
                "player/standing.png", collider_uncrouched.get_surface(color)
            ),
            running=txt_dao.load_sequence("player/running", 4),
            jumping=txt_dao.load("player/jumping.png"),
        )

        super().__init__(
            render, pos_comp, self.__move, self.__collision["uncrouched"], self.__slide
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
