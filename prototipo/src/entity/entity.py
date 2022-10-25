from pygame import Vector3


class Entity:
    def __init__(self, id: int):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        return self.id == other.id
