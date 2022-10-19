from typing import List

from .obstacle import Obstacle
from .player import Player
from .powerup import PowerUp


class EntityManager:
    obstacles: List[Obstacle]
    power_ups: List[PowerUp]
    player: Player
