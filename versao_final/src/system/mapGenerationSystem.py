from math import ceil
from random import randint
from typing import Dict, List, Type

from ..dao import MapDAO
from ..entity import (
    Background,
    BigBush,
    Bike,
    Bridge,
    Bus,
    Car,
    Handrail,
    Obstacle,
    PartyAdsTable,
    SmallBush,
    Student,
    Water,
)
from ..components import RenderComponent
from ..icontrol import IControl
from .system import System


class MapGenerationSystem(System):
    __last_obstacle_z_pos: int
    __last_background_z_pos: int
    __patterns: List[List[str]]
    __obstacle_map: Dict[str, Type[Obstacle]]

    def __init__(self, control: IControl):
        super().__init__(control)

        self.__last_obstacle_z_pos = 0
        self.__last_background_z_pos = 0

        self.__obstacle_map = {
            "B": Bridge,
            "W": Water,
            "C": Car,
            "H": Handrail,
            "P": PartyAdsTable,
            "S": Student,
            "E": SmallBush,
            "F": BigBush,
            "G": Bike,
            "O": Bus,
            "X": None,
            " ": None,
        }

        path = "easy.json"
        dao = MapDAO()

        map = dao.load(path)

        self.__patterns = map["patterns"]
    
    def setup(self):
        self.__last_obstacle_z_pos = 0
        self.__last_background_z_pos = -self.control.screen.size[1]

    def add_pattern(self, pattern):
        ...

    @property
    def z_pos(self):
        lane_width = self.control.map.lane_width
        screen = self.control.screen

        z_pos = screen.cam.pos.y + screen.size[1] + 0

        return ceil(z_pos / lane_width) * lane_width

    def update(self):
        z_pos = self.z_pos

        while z_pos > self.__last_obstacle_z_pos:
            self.spawn_obstacles()

        while z_pos > self.__last_background_z_pos:
            self.spawn_background()
        
    def skip_tiles(self, amount: int):
        self.__last_obstacle_z_pos += self.control.config.lane_width * amount

    def spawn_obstacles(self):
        z = self.__last_obstacle_z_pos
        lane_width = self.control.map.lane_width

        pattern_i = randint(0, len(self.__patterns) - 1)
        pattern = self.__patterns[pattern_i]

        for line_i, line in enumerate(pattern[::-1]):
            line_z = z + lane_width * line_i

            for lane_i, char in enumerate(line):
                obstacle_class = self.__obstacle_map.get(char)

                if obstacle_class is None:
                    continue

                x = self.control.map.lanes[lane_i]

                obstacle = obstacle_class(pos=(x, 0, line_z))

                self.control.entities.add_entity(obstacle)

        self.__last_obstacle_z_pos += len(pattern) * lane_width

    def spawn_background(self):
        z = self.__last_background_z_pos
        x = self.control.map.center

        background = Background(pos=(x, -1, z))

        render = background.get_component(RenderComponent)
        background_height = render.size[1]

        self.control.entities.add_entity(background)

        self.__last_background_z_pos += background_height

    @property
    def obstacle_map(self):
        return self.__obstacle_map

    @property
    def patterns(self):
        return self.__patterns
