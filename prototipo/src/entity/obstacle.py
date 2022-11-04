from ..components import CollisionComponent, MoveComponent, RenderComponent
from ..library import CubeCollider
from .entity import Entity


class Obstacle(Entity):
    def __init__(self, pos, size, velocity=(0, 0, 0), color="#ffff00"):
        render = RenderComponent((size[0], size[1] + size[2]), color)
        move = MoveComponent(pos, velocity)

        collider = CubeCollider(move.pos, size)
        collision = CollisionComponent(collider)

        super().__init__(render, move, collision)


class Student(Obstacle):
    ...


class Wall(Obstacle):
    ...


class Bush(Obstacle):
    ...
