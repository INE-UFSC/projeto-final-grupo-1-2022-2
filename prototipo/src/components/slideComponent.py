
from .component import Component
import pygame as pg

class SlideComponent(Component):
    def __init__(self):
        self.__progress = 0
        self.__start_pos = pg.Vector2()
        self.__end_pos = pg.Vector2()
    
    @property
    def progress(self):
        return self.__progress

    @property
    def start_pos(self):
        return self.__start_pos
    
    @property
    def end_pos(self):
        return self.__end_pos

    def set_progress(self, progress: int):
        self.__progress = progress
