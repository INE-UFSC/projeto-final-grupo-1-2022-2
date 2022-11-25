from ..dao import LeaderboardDAO
from .moveSystem import MoveComponent
from .system import System


class ScoreSystem(System):
    __leaderboard = LeaderboardDAO()

    def update(self):
        player = self.control.entities.player
        player_pos = player.get_component(MoveComponent).pos

        score = int((player_pos.z) / 100)
        player_name = self.control.config.player_name
        difficulty = self.control.config.difficulty

        self.__leaderboard.update(player_name,difficulty,score)
    


