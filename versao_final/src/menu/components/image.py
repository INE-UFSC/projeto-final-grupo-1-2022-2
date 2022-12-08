import pygame as pg

from .component import MenuComponent
from ...dao import TextureDAO

# TODO
# Usar um DAO
class Image(MenuComponent):
    def __init__(self, path: str, alpha: bool = False, pos = None,spacing = None, key=None):
        image = TextureDAO().load(path)
        self.__alpha = alpha
        super().__init__(pos,image.get_size(), image,spacing=spacing, key=key)

    def convert(self):
        self.surface.convert() if not self.__alpha else self.surface.convert_alpha()
        
