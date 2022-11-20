import pygame as pg

from ..components import MoveComponent, SlideComponent
from ..library import Listener
from .system import System


# TODO
# adicionar encadeamento de movimentos.
class MoveControlSystem(System):
    def setup(self):
        self.__next_move = None
        self.__time_on_crouch = 0

    @Listener.on(pg.KEYDOWN)
    def jump(self, event: pg.event.Event):
        if event.key != pg.K_UP:
            return

        player = self.control.entities.player
        move = player.get_component(MoveComponent)

        if not move.on_ground:
            return
        elif player.is_crouched:
            self.__time_on_crouch = 0
            player.uncrouch()
            return

        move.velocity.y = self.control.config.jump_force

    @Listener.on(pg.KEYDOWN)
    def down(self, event: pg.event.Event):
        if event.key != pg.K_DOWN:
            return

        player = self.control.entities.player
        move = player.get_component(MoveComponent)

        if not move.on_ground:
            move.velocity.y = -self.control.config.jump_force
        else:
            self.__time_on_crouch += self.control.clock.get_time()
            player.crouch()

    @Listener.on(pg.KEYDOWN)
    def move(self, event: pg.event.Event):
        if event.key not in (pg.K_LEFT, pg.K_RIGHT):
            return

        direction = -1 if event.key == pg.K_LEFT else 1

        slide_length = self.control.map.lane_width
        slide_duration = self.control.config.slide_duration

        delta_x = slide_length * direction

        self.__next_move = (delta_x, slide_duration)

    def update(self):
        player = self.control.entities.player

        slide = player.get_component(SlideComponent)
        move = player.get_component(MoveComponent)

        if self.__next_move and not slide.active:
            delta_x, duration = self.__next_move

            start_x = move.pos.x
            end_x = start_x + delta_x

            if self.control.map.is_inside(end_x):
                slide.set(start_x, end_x, duration)

            self.__next_move = None

        if slide.active:
            slide.add_progress(self.control.deltatime)

            move.pos.x = slide.get_interpolated_x()

            if slide.done:
                slide.reset()

        crouch_duration = self.control.config.crouch_duration
        if self.__time_on_crouch > crouch_duration:
            player.uncrouch()
            self.__time_on_crouch = 0

        if player.is_crouched:
            self.__time_on_crouch += self.control.clock.get_time()
