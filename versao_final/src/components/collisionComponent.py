"""
Classe collision component
"""
import pygame as pg

from .component import Component


class CollisionComponent(Component):
    def __init__(self, shape):
        self.__shape = shape
    
    @property
    def shape(self):
        return self.__shape