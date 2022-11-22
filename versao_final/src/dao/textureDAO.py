from pathlib import Path
from typing import Callable, Dict, Tuple, Union

import pygame as pg

from .resourceDAO import ResourceDAO


class TextureDAO(ResourceDAO):
    _cache: Dict[str, pg.Surface]
    _dir: str = "textures"

    def load(
        self,
        relative_path: Union[str, Tuple[str]],
        default: Union[pg.Surface, Callable[..., pg.Surface]] = None,
    ):
        path = self.get_path(relative_path)

        if path not in self._cache:
            try:
                surface = pg.image.load(path)
            except (FileNotFoundError, pg.error):
                # default is a supplier (lazy evaluation)
                if isinstance(default, Callable):
                    default = default()

                if not default:
                    return

                surface = default

            self._cache[path] = surface

        return self._cache.get(path)

    def save(self, relative_path: Union[str, Tuple[str]], surface: pg.Surface):
        path = self.get_path(relative_path)
        
        Path(path).parent.mkdir(parents=True, exist_ok=True)

        pg.image.save(surface, path)

    def save_all(self):
        for path, surface in self._cache.items():
            self.save(path, surface)
