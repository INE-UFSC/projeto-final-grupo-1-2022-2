from typing import Union

import pygame as pg

from .config import Config
from .entity import EntityManager, Map
from .icontrol import IControl
from .leaderboard import Leaderboard
from .library import Camera, EventBus, Keyboard, Mouse, Screen
from .scene import Scene, SceneManager


class GameControl(IControl):
    __config: Config
    __event: EventBus
    __keyboard: Keyboard
    __mouse: Mouse
    __clock: pg.time.Clock

    __scene: SceneManager
    __entities: EntityManager
    __map: Map
    __leaderboard: Leaderboard
    __running: bool

    __framerate: int
    __deltatime: int
    __max_deltatime: int

    def __init__(self):
        self.__running = False
        self.__deltatime = 0

        cfg = Config()
        self.__config = cfg

        self.__event = EventBus()
        self.__entities = EntityManager()
        self.__map = Map(cfg.lane_width, cfg.lane_amount)
        self.__scene = SceneManager()
        self.__clock = pg.time.Clock()
        self.__screen = Screen(
            self.config.screen_size, Camera(self.config.camera_offset)
        )

    def is_running(self):
        return self.__running

    def stop_running(self):
        self.__running = False

    def start(self):
        self.__running = True
        self.__event.subscribe(pg.QUIT, lambda _: self.stop_running())
        self.__event.subscribe("*", self.__forward_event_to_scene)

        self.__screen.start()

    def __forward_event_to_scene(self, event_name: str, *args, **kwargs):
        current_scene = self.__scene.current_scene

        if current_scene is not None:
            current_scene.emit(event_name, *args, **kwargs)

    def tick(self):
        delta = self.__clock.tick(self.__config.framerate) / 1000

        self.__deltatime = min(delta, self.__config.max_deltatime)

    def update(self):
        self.tick()

        self.__scene.update_transition()

        self.__event.update()
        self.__scene.update()
        self.__screen.update()

    def transition(self, to_scene: Union["Scene", str, None]):
        return self.__scene.transition(to_scene)

    @property
    def config(self):
        return self.__config

    @property
    def event(self):
        return self.__event

    @property
    def clock(self):
        return self.__clock

    @property
    def deltatime(self):
        return self.__deltatime

    @property
    def scene(self):
        return self.__scene

    @property
    def screen(self):
        return self.__screen

    @property
    def entities(self):
        return self.__entities

    @property
    def map(self):
        return self.__map
