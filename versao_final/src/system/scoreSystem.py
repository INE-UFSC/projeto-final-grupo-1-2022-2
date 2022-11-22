from .moveSystem import MoveComponent
from .system import System


class ScoreSystem(System):
    def update(self):
        player = self.control.entities.player
        player_pos = player.get_component(MoveComponent).pos

        print(int((player_pos.z) / 100))
