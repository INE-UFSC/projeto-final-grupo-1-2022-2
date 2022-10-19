from pygame import Vector3


class Entity:
    pos: Vector3
    size: Vector3

    def update(self):
        ...

    def render(self):
        ...
