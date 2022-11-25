
import json
import time
from pathlib import Path
from typing import Dict

import pygame as pg

from .resourceDAO import ResourceDAO


class LeaderboardDAO(ResourceDAO):
    _cache: Dict[str, pg.Surface]
    _path = "leaderboard.json"

    def load(self):
        path = self.get_path(self._path)

        if path not in self._cache:
            try:
                leaderboard = json.load(open(path, "rt", encoding="utf-8"))
                print(leaderboard)
            except FileNotFoundError:
                return
            except json.decoder.JSONDecodeError:
                # use logger
                print(f"[ERROR] invalid json format for leaderboard in file '{self._path}'.")
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
