from typing import Tuple


class Config:
    screen_size: Tuple[int, int] = (1280, 760)

    lane_amount: int = 3
    lane_width: int = 120

    framerate: int = 60
    max_deltatime: float = 0.1

    destruction_distance: int = 1000

    slide_duration: float = 0.25
    gravity: float = -1600
    jump_force: float = 580
    crouch_duration: int = 1000  # crouch duration in milliseconds

    camera_y_offset: int = -100
