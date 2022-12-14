from ..dao import LeaderboardDAO
from .moveSystem import PosComponent
from .system import System


class ScoreSystem(System):
    __leaderboard = LeaderboardDAO()

    def update(self):
        player = self.control.entities.player
        player_pos = player.get_component(PosComponent).value

        score = int((player_pos.z) / 100)
        player_name = LeaderboardDAO().get_player_name()
        if player_name is None:
            player_name = self.control.config.default_player_name
        difficulty = self.control.config.difficulty

        LeaderboardDAO().set_player_score(score)

        if score > LeaderboardDAO().get_player_highscore(player_name, difficulty):
            self.__leaderboard.update(player_name, difficulty, score)
