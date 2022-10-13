from pygame import Vector3


class Object:
    pos: Vector3
    size: Vector3

    def update(self):
        ...

    def render(self):
        ...
