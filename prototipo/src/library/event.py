import pygame as pg

from .listener import Listener


class EventBus(Listener):
    def update(self):
        for event in pg.event.get():
            self.emit(event.type, event)
