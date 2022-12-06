from ..config import Config

import pygame as pg

class Map:
    def __init__(self, lane_width: float, lane_amount: int, center_x: float = None):
        self.__lane_width = lane_width
        self.__lane_amount = lane_amount

        self.__center = self.total_width // 2 if center_x is None else center_x

    @property
    def lane_width(self):
        return self.__lane_width

    @property
    def lane_amount(self):
        return self.__lane_amount

    @property
    def center(self):
        return self.__center

    @property
    def total_width(self):
        return self.__lane_width * self.__lane_amount

    @property
    def total_boundary(self):
        half_width = self.total_width // 2

        return (self.__center - half_width, self.__center + half_width)

    @property
    def lanes(self):
        start, _ = self.total_boundary

        return tuple(
            start + (0.5 + i) * self.__lane_width for i in range(self.__lane_amount)
        )

    @property
    def lane_boundaries(self):
        half_lane = self.__lane_width // 2

        return tuple((x - half_lane, x + half_lane) for x in self.lanes)

    def is_inside(self, x: float):
        min, max = self.total_boundary

        return min <= x <= max
    
    def get_default_surface(self):
        size = Config().screen_size
        surface = pg.Surface(size)

        grass_color = pg.Color("#96fa2a")
        lane_color = pg.Color("#f2cf4e")
        line_color = pg.Color("#dbb939")

        start_x = size[0] // 2 - self.total_width // 2

        surface.fill(grass_color)

        pg.draw.rect(surface, lane_color, (start_x, 0, self.total_width, size[1]))

        pg.draw.line(surface, line_color, (start_x, 0), (start_x, size[1]), 3)
        for _, right_x in self.lane_boundaries:
            x = start_x + right_x
            pg.draw.line(surface, line_color, (x, 0), (x, size[1]), 3)

        return surface
