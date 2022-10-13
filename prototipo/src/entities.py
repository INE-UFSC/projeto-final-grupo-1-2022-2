from typing import List

from .object import Obstacle, Player, PowerUp


class GameEntities:
    obstacles: List[Obstacle]
    power_ups: List[PowerUp]
    player: Player
