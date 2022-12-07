from random import choice
from typing import Callable, List
import pygame as pg

from ..components import CollisionComponent, PosComponent, MoveComponent, RenderComponent
from ..library import CubeCollider, class_name, snake_case
from ..dao import TextureDAO
from .entity import Entity


class Obstacle(Entity):
    _textures = None

    def __init__(
        self,
        pos,
        size,
        velocity=None,
        color="#ffff00",
        climb_height: float = -1,
        surface: pg.Surface = None,
        alpha: bool = False
    ):
        pos_comp = PosComponent(pos)
        move = MoveComponent(velocity) if velocity else None

        collider = CubeCollider(pos_comp.value, size)
        collision = CollisionComponent(collider, climb_height)

        if surface is None:
            surface = self.get_texture(lambda: collider.get_surface(color))

        render = RenderComponent(surface, alpha=alpha)

        super().__init__(pos_comp, move, collision, render)
    
    @classmethod
    def get_texture(cls, default: Callable[..., pg.Surface]):
        name = snake_case(cls.__name__)

        if cls._textures is None:
            cls._textures = TextureDAO().load_many(name)

        surface = choice(cls._textures) if cls._textures else None

        if surface is None:
            texture_path = f"{name}.png"
            surface = TextureDAO().load(texture_path, default)
        
        return surface


class Handrail(Obstacle):
    """
    Obstacle that represents a handrail
    """
    def __init__(self, pos, size=[10, 50, 120], color="#F5BB00"):
        self.__pos_dislocated = (pos[0]+ 40, pos[1], pos[2])
        super().__init__(self.__pos_dislocated, size, color=color, alpha=True)


class PartyAdsTable(Obstacle):
    """
    Obstacle that represents a party advertisement table
    """
    def __init__(self, pos, size=[100, 50, 50], color="#ffffff"):
        super().__init__(pos, size, color=color, alpha=True)


class SmallBush(Obstacle):
    """
    Obstacle that represents a small bush
    """
    def __init__(self, pos, size=[50, 50, 10], color="#60f731"):
        super().__init__(pos, size, color=color, alpha=True)


class BigBush(Obstacle):
    """
    Obstacle that represents a big bush
    """
    def __init__(self, pos, size=[120, 80, 50], color="#09ad19"):
        super().__init__(pos, size, color=color, alpha=True)


class Bike(Obstacle):
    """
    Obstacle that represents a bike
    """
    def __init__(self, pos, size=[20, 50, 60], velocity=(0, 0, 0), color="#003B36"):
        super().__init__(pos, size, velocity, color, alpha=True)


class Student(Obstacle):
    """
    Obstacle that represents a student
    """
    def __init__(self, pos, size=[60, 110, 4], color="#ffc294"):
        super().__init__(pos, size, color=color, alpha=True)


class Car(Obstacle):
    """
    Obstacle that represents a car
    """
    def __init__(self, pos, size=[100, 60, 110], velocity=(0, 0, 0), color="#222222"):
        self.__climb_height = 20
        super().__init__(pos, size, velocity, color, self.__climb_height, alpha=True)


class Bus(Obstacle):
    """
    Obstacle that represents a car
    """
    def __init__(self, pos, size=[100, 130, 360], velocity=(0, 0, 0), color="#222e50"):
        self.__climb_height = 20
        super().__init__(pos, size, velocity, color, self.__climb_height)


class Bridge(Obstacle):
    """
    Obstacle that represents a bridge
    """
    def __init__(self, pos, size=[120, 10, 240], color="#99571d"):
        climb_height = 10
        super().__init__(pos, size, color=color, climb_height=climb_height)

class Water(Obstacle):
    """
    Obstacle that represents water
    """
    def __init__(self, pos, size=[120, 1, 120], color="#54beff"):
        super().__init__(pos, size, color=color)



