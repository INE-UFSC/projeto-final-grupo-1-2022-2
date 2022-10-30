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
    
    @property
    def map_width(self):
        config = self.control.config
        return config.lane_width * config.lane_amount
    
    @property
    def map_center(self):
        return self.control.screen.center
    
    @property
    def map_x_boundary(self):
        half_width = self.map_width // 2
        center_x, _ = self.map_center

        return (center_x - half_width, center_x + half_width)
    

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
        lane_width = self.control.config.lane_width
        lane_amount = self.control.config.lane_amount

        map_left_x, _ = self.map_x_boundary

        lane_i = randint(0, lane_amount-1)

        x = map_left_x + lane_i * lane_width

        entity = Entity(
            RenderComponent((lane_width, lane_width), "#ffff00"), 
            MoveComponent((x, 0, z), (0, 0, 0), True)
        )

        self.control.entities.add_entity(entity)




    