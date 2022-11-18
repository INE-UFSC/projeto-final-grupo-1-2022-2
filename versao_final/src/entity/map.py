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
