from .entity import Entity
from ..components import RenderComponent, MoveComponent, SlideComponent

class Player(Entity):
    def __init__(self):
        render = RenderComponent((100, 200), "#ff0000")
        move = MoveComponent((200, 0, 200), (0, 0, 200), True)
        slide = SlideComponent()

        super().__init__(render, move, slide)
