from .entity import Entity
from ..components import RenderComponent, MoveComponent, CollisionComponent
from ..library import CubeCollider


class Obstacle(Entity):
    def __init__(self, pos, size, velocity = (0, 0, 0), color = "#ffff00"):
        render = RenderComponent((size[0], size[1] + size[2]), color)
        move = MoveComponent(pos, velocity, True)

        collider = CubeCollider(move.pos, size)
        collision = CollisionComponent(collider)

        super().__init__(render, move, collision)



class Student(Obstacle):
    ...


class Wall(Obstacle):
    ...


class Bush(Obstacle):
    ...
