from ..entity import Player
from ..components import MoveComponent, SlideComponent
from .system import System
from ..library import Listener

import pygame as pg



class MoveControlSystem(System):
    def update(self):
        player = self.control.entities.player
        
        player.get_component(MoveComponent).pos.z
    
    @Listener.on(pg.KEYDOWN)
    def jump(self, event: pg.event.Event):
        if event.key != pg.K_UP:
            return

        player = self.control.entities.player
        move = player.get_component(MoveComponent)
    
        if not move.on_ground:
            return
    
        move.velocity.y = 50
        move.set_on_ground(False)

    @Listener.on(pg.KEYDOWN)
    def down(self, event: pg.event.Event):
        if event.key != pg.K_DOWN:
            return
        
        #TODO

    @Listener.on(pg.KEYDOWN)
    def move(self, event: pg.event.Event):
        if event.key not in (pg.K_LEFT, pg.K_RIGHT):
            return
        
        direction = -1 if event.key == pg.K_LEFT else 1

        player = self.control.entities.player
        move = player.get_component(MoveComponent)
        slide = player.get_component(SlideComponent)

        TILE_SIZE = 100

        start_pos = move.pos
        end_pos = move.pos + (TILE_SIZE * direction, 0, 0)

        move.pos.update(end_pos)

        # TODO: Implementar animação de movimento
        # slide.start_pos.update(start_pos)
        # slide.end_pos.update(end_pos)
        # slide.set_progress(0)
        




    