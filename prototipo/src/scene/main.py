from .scene import IControl, Scene
from .system import RenderSystem
from ..entity import Player
import pygame as pg



class MainScene(Scene):
    def __init__(self, control: IControl):
        menu = None
        systems = [
            RenderSystem()
        ]

        super().__init__(control, menu, systems)
    
    def enter(self):
        player = Player()
        self.control.entities.add_entity(player)

    def update(self):
        for system in self.systems:
            system.update(self.control)