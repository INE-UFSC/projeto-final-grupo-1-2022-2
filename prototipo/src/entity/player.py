from .entity import Entity
from ..components import RenderComponent, MoveComponent

class Player(Entity):
    def __init__(self):
        render = RenderComponent((100, 200), "#ffaaaa")
        move = MoveComponent((200, 200, 200), (0, 0, 0), True)

        super().__init__(render, move)
