from typing import Tuple


class Config:
    screen_size: Tuple[int, int] = (1280, 760)

    lane_amount: int = 4
    lane_width: int = 100

    framerate: int = 60
    max_deltatime: float = 0.1

    destruction_distance: int = 1000

    slide_duration: float = 0.3
    gravity: float = -1000
    jump_force: float = 800
    camera_offset: Tuple[int, int] = (0, -100)
