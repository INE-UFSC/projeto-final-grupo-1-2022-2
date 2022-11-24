from typing import Dict

import pygame as pg

from ..entity import Player
from ..icontrol import IControl
from ..library import Listener
from ..menu import GameplayMenu, PauseMenu
from ..system import (
    CameraSystem,
    CollisionSystem,
    EntityDestructionSystem,
    MapGenerationSystem,
    MoveControlSystem,
    MoveSystem,
    RenderSystem,
    ScoreSystem,
)
from .scene import Scene


class MainScene(Scene):
    def __init__(self, control: IControl):
        menus = {"gameplay": GameplayMenu(control), "pause": PauseMenu(control)}
        self.__paused = False
        systems = [
            MoveControlSystem(control),
            MoveSystem(control),
            CameraSystem(control),
            MapGenerationSystem(control),
            CollisionSystem(control),
            EntityDestructionSystem(control),
            RenderSystem(control),
            ScoreSystem(control),
        ]

        super().__init__(control, menus, systems)

    def enter(self):
        self.current_menu = self.menus["gameplay"]
        lane_i = self.control.map.lane_amount // 2
        mid_lane_x = self.control.map.lanes[lane_i]
        player = Player(pos=(mid_lane_x, 0, 0))

        self.control.entities.set_player(player)
        self.control.entities.add_entity(player)

        camera = self.control.screen.cam
        offset = (
            mid_lane_x - self.control.screen.size[0] // 2,
            self.control.config.camera_y_offset,
        )
        camera.offset = offset

        for system in self.systems:
            system.setup()

    def update(self):
        if not self.__paused:
            for system in self.systems:
                system.update()

        if self.next_scene is not None:
            self.control.transition(self.next_scene)
            self.next_scene = None

    def render(self):
        if self.current_menu is not None:
            self.current_menu.render()

    def leave(self):
        self.control.entities.clear()

    @Listener.on("player_collision")
    def __game_over(self, player, obstacle):
        self.next_scene = self.control.scene.scenes["end"]

    @Listener.on(pg.KEYDOWN)
    def __toggle_pause(self, event: pg.event.Event):
        if event.key == pg.K_ESCAPE:
            if self.__paused:
                self.__resume()
            else:
                self.current_menu = self.menus["pause"]
                self.__paused = True

    @Listener.on("Resume")
    def __resume(self):
        self.__paused = False
        self.current_menu = self.menus["gameplay"]

    @Listener.on("Quit")
    def __stop_running(self):
        self.control.stop_running()
