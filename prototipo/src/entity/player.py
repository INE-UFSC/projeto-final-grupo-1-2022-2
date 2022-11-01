from .entity import Entity
from ..components import RenderComponent, MoveComponent, SlideComponent, CollisionComponent
from ..library import CubeCollider

class Player(Entity):
    def __init__(self, pos):
        render = RenderComponent((100, 200), "#ff0000")
        move = MoveComponent(pos, (0, 0, 200), True)
        slide = SlideComponent()

        collider = CubeCollider(move.pos, (100, 200, 1))
        collision = CollisionComponent(collider)

        super().__init__(render, move, collision, slide)
