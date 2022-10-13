from typing import List

from .component import MenuComponent


class Menu:
    components: List[MenuComponent]

    def update(self):
        ...
