from .system import System
from ..entity import Entity
from ..components import MoveComponent, RenderComponent
from ..icontrol import IControl

from random import randint
from typing import Tuple
import pygame as pg



class MapGenerationSystem(System):
    __min_distance: float
    __last_z_pos: int

    def __init__(self, control: IControl):
        super().__init__(control)

        self.__min_distance = 200
        self.__last_z_pos = 0

    def update(self):
        entities = self.control.entities
        screen = self.control.screen

        z_pos = screen.cam.pos.y + screen.size[1]

        delta_z = z_pos - self.__last_z_pos

        if delta_z < self.__min_distance:
            return

        self.spawn(z_pos)
        self.__last_z_pos = z_pos

    def spawn(self, z: int):
        lane_width = self.control.map.lane_width
        lane_amount = self.control.map.lane_amount

        lane_i = randint(0, lane_amount - 1)
        x = self.control.map.lanes[lane_i]

        entity = Entity(
            RenderComponent((lane_width, lane_width), "#ffff00"), 
            MoveComponent((x, 0, z), (0, 0, 0), True)
        )

        self.control.entities.add_entity(entity)
