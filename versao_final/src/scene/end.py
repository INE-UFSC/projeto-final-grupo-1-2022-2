from typing import Dict

import pygame as pg

from ..icontrol import IControl
from ..library import Listener
from ..menu import EndMenu
from .scene import Scene


class EndScene(Scene):
    def __init__(self, control: IControl):
        menus = {"end": EndMenu(control)}

        super().__init__(control, menus, [])

    def enter(self):
        self.current_menu = self.menus["end"]
        super().enter()


    @Listener.on("Play")
    def __play_again(self):
        self.next_scene = self.control.scene.scenes["main"]

    @Listener.on("Start")
    def __start_menu(self):
        self.next_scene = self.control.scene.scenes["start"]

    @Listener.on("Quit")
    def __stop_running(self):
        self.control.stop_running()
