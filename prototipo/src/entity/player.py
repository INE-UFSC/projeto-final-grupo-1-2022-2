from .entity import Entity
from ..components import RenderComponent, MoveComponent, SlideComponent

class Player(Entity):
    def __init__(self, pos):
        render = RenderComponent((100, 200), "#ff0000")
        move = MoveComponent(pos, (0, 0, 200), True)
        slide = SlideComponent()

        super().__init__(render, move, slide)
