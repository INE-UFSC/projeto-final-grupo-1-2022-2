from typing import Tuple

class Config:
    screen_size: Tuple[int, int] = (1280, 760)

    lane_amount: int = 3
    lane_width: int = 100
    
    framerate: int = 60
    max_deltatime: float = 0.1