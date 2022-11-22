
from functools import cached_property
from pathlib import Path
from typing import Any, Dict, Tuple, Union

from ..library import Singleton


class ResourceDAO(metaclass=Singleton):
    _cache: Dict[Any, Any]
    _dir: str = ""
    
    def __init__(self):
        dir = Path(self._dir)
        self.__directory = dir if dir.is_absolute() else self.resources_dir / dir

        self._cache = {}
    
    def get_path(self, relative: Union[str, Tuple[str], Path]) -> str:
        if not isinstance(relative, tuple):
            relative = (relative,)

        return str(self.__directory / Path(*relative))

    
    @cached_property
    def resources_dir(self):
        return Path(__file__).parent.parent.parent / "resources"

    @property
    def directory(self):
        return self.__directory