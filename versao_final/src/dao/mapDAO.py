from pathlib import Path
from typing import Callable, Dict, Tuple, Union

import pygame as pg
import json

from .resourceDAO import ResourceDAO


class MapDAO(ResourceDAO):
    _cache: Dict[str, pg.Surface]
    _dir: str = "maps"

    def load_all(self):
        ...

    def load(self, relative_path: Union[str, Tuple[str]]):
        path = self.get_path(relative_path)

        if path not in self._cache:
            try:
                map = json.load(open(path, "rt", encoding="utf-8"))
            except FileNotFoundError:
                return
            except json.decoder.JSONDecodeError:
                # use logger
                print(
                    f"[ERROR] invalid json format for map pattern in file '{relative_path}'."
                )
                return

            self._cache[path] = map

        return self._cache.get(path)

    def save(self, relative_path: Union[str, Tuple[str]], map_obj: dict):
        path = Path(self.get_path(relative_path))

        path.parent.mkdir(parents=True, exist_ok=True)

        txt = json.dumps(map_obj)

        path.write_text(txt, encoding="utf-8")

    def save_all(self):
        for path, map_obj in self._cache.items():
            self.save(path, map_obj)
