import json
import time
from collections import namedtuple
from pathlib import Path
from typing import Dict, List, NamedTuple

import pygame as pg

from .resourceDAO import ResourceDAO

Score = namedtuple("Score", ["name", "value"])
Score_annotation = NamedTuple("Score", [("name", str), ("value", int)])


class LeaderboardDAO(ResourceDAO):
    _cache: Dict[str, pg.Surface]
    _path = "leaderboard.json"

    def __init__(self):
        super().__init__()
        self.load()

    def load(self):
        path = self.get_path(self._path)

        if path not in self._cache:
            try:
                leaderboard = json.load(open(path, "rt", encoding="utf-8"))
            except FileNotFoundError:
                return
            except json.decoder.JSONDecodeError:
                # use logger
                print(
                    f"[ERROR] invalid json format for leaderboard in file '{self._path}'."
                )
                return

            self._cache = leaderboard

        return self._cache.get(path)

    def update(self, name, difficulty, score):
        players = self._cache.setdefault("players", {})
        player = players.setdefault(name, {})
        difficulty_obj = player.setdefault(difficulty, {})

        difficulty_obj["highscore"] = score
        difficulty_obj["timestamp"] = time.time()

    def save(self):
        path = Path(self.get_path(self._path))
        path.parent.mkdir(parents=True, exist_ok=True)

        txt = json.dumps(self._cache)

        path.write_text(txt, encoding="utf-8")

    def get_sorted_list(self, difficulty: str) -> List[Score_annotation]:
        players_score = []

        for name, player_dict in self._cache.get("players", {}).items():
            points = player_dict.get(difficulty, {}).get("highscore", 0)
            players_score.append(Score(name, points))

        return sorted(players_score, key=lambda p: p.value, reverse=True)

    
    
    def get_player_highscore(self,name: str, difficulty: str):
        players = self._cache.get("players", {})
        player = players.get(name, {})
        diff = player.get(difficulty, {})
        score = diff.get("highscore", -1)
        return score

    def get_player_score(self):
        return self._cache.get("player_score", 0)

    def set_player_score(self, score: int):
        self._cache["player_score"] = score

    def get_player_name(self):
        return self._cache.get("player_name", None)

    def set_player_name(self, name: str):
        self._cache["player_name"] = name    
