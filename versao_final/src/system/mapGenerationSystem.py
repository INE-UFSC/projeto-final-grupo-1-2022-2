from .system import System
from ..icontrol import IControl
from typing import Dict, List, Type
from random import randint
from ..entity import Bus, Car, Student, Bridge, Handrail, PartyAdsTable, SmallBush, BigBush, Bike, Obstacle


class MapGenerationSystem(System):
    __wait_distance: float
    __last_z_pos: int
    __patterns: List[List[str]]
    __obstacle_map: Dict[str, Type[Obstacle]]
    
    def __init__(self, control: IControl):
        super().__init__(control)

        self.__wait_distance = 200
        self.__last_z_pos = 0

        self.__obstacle_map = {
            "B" : Bridge,
            "C" : Car,
            "H" : Handrail,
            "P" : PartyAdsTable,
            "S" : Student,
            
            "E" : SmallBush,
            "F" : BigBush,
            "G" : Bike,
            "O" : Bus,

            "X" : None,
            " " : None,
        }

        self.__patterns = [
            # [
            #     "  CC",
            #     "    ",
            #     "CC  ",
            # ],
            [
                "C   "
            ]
            # [
            #     " O  ",
            #     " O  ",
            #     " O  ",
            #     " X  ",
            #     " X  ",
            #     " O  ",
            # ],
        ]
    
    def add_pattern(self, pattern):
        ...

    def update(self):
        lane_width = self.control.map.lane_width
        screen = self.control.screen

        z_pos = screen.cam.pos.y + screen.size[1]
        z_pos = (z_pos // lane_width) * lane_width

        delta_z = z_pos - self.__last_z_pos

        if delta_z >= self.__wait_distance:
            length = self.spawn(z_pos)

            self.__wait_distance = length
            self.__last_z_pos = z_pos

    def spawn(self, z: int):
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
        
        return len(pattern) * lane_width


    @property
    def obstacle_map(self):
        return self.__obstacle_map
    @property
    def patterns(self):
        return self.__patterns
        
