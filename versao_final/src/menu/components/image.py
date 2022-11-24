import pygame as pg

from .component import MenuComponent


# TODO
# Usar um DAO
class Image(MenuComponent):
    def __init__(self, path: str):
        surfac = pg.image.load()
