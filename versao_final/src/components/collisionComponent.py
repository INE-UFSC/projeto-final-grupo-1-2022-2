"""
Classe collision component
"""
import pygame as pg

from .component import Component
from ..library import ColliderShape


class CollisionComponent(Component):
    __climb_height: float
    __shape: ColliderShape

    def __init__(self, shape, climb_height=-1):
        self.__shape = shape
        self.__climb_height = climb_height
    
    @property
    def shape(self):
        return self.__shape

    @property
    def climb_height(self):
        return self.__climb_height