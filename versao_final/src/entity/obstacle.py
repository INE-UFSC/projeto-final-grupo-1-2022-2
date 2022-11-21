from ..components import CollisionComponent, MoveComponent, RenderComponent
from ..library import CubeCollider
from .entity import Entity


class Obstacle(Entity):
    def __init__(self, pos, size, velocity=(0, 0, 0), color="#ffff00", climb_height: float = -1):
        self.__move = MoveComponent(pos, velocity)

        self.__collider = CubeCollider(self.__move.pos, size)
        self.__collision = CollisionComponent(self.__collider, climb_height)

        self.__render = RenderComponent.from_cube(self.__collider, color)

        super().__init__(self.__render, self.__move, self.__collision)


class Handrail(Obstacle):
    """
    Obstacle that represents a handrail
    """
    def __init__(self, pos, size=[10, 50, 100], velocity=(0, 0, 0), color="#F5BB00"):
        self.__pos_dislocated = (pos[0]+ 40, pos[1], pos[2])
        super().__init__(self.__pos_dislocated, size, velocity, color)


class PartyAdsTable(Obstacle):
    """
    Obstacle that represents a party advertisement table
    """
    def __init__(self, pos, size=[100, 50, 50], velocity=(0, 0, 0), color="#ffffff"):
        super().__init__(pos, size, velocity, color)


class SmallBush(Obstacle):
    """
    Obstacle that represents a small bush
    """
    def __init__(self, pos, size=[120, 50, 50], velocity=(0, 0, 0), color="#003B36"):
        super().__init__(pos, size, velocity, color)


class BigBush(Obstacle):
    """
    Obstacle that represents a big bush
    """
    def __init__(self, pos, size=[240, 50, 50], velocity=(0, 0, 0), color="#003B36"):
        super().__init__(pos, size, velocity, color)


class Bike(Obstacle):
    """
    Obstacle that represents a bike
    """
    def __init__(self, pos, size=[20, 50, 50], velocity=(0, 0, -50), color="#003B36"):
        super().__init__(pos, size, velocity, color)


class Student(Obstacle):
    """
    Obstacle that represents a student
    """
    def __init__(self, pos, size=[60, 50, 50], velocity=(0, 0, 0), color="#482728"):
        super().__init__(pos, size, velocity, color)


class Car(Obstacle):
    """
    Obstacle that represents a car
    """
    def __init__(self, pos, size=[100, 60, 100], velocity=(0, 0, -100), color="#222222"):
        self.__climb_height = 20
        super().__init__(pos, size, velocity, color, self.__climb_height)


class Bus(Obstacle):
    """
    Obstacle that represents a car
    """
    def __init__(self, pos, size=[100, 130, 400], velocity=(0, 0, -100), color="#222e50"):
        self.__climb_height = 20
        super().__init__(pos, size, velocity, color, self.__climb_height)


class Bridge(Obstacle):
    """
    Obstacle that represents a bridge
    """
    def __init__(self, pos, size=[100, 240, 50], velocity=(0, 0, 0), color="#576066"):
        super().__init__(pos, size, velocity, color)



