from ..entity import Player
from ..components import MoveComponent
from .system import System
from ..library import Listener

import pygame as pg



class MoveControlSystem(System):
    def update(self):
        player = self.control.entities.player
        
        player.get_component(MoveComponent).pos.z
    
    @Listener.on(pg.KEYDOWN)
    def jump(self, event: pg.event.Event):
        if event.key == pg.K_UP:
            player = self.control.entities.player

            move = player.get_component(MoveComponent)

            move.velocity.y = 50

    