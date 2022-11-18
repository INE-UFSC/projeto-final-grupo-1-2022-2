from typing import Tuple, Union

import pygame as pg

from .component import Component


def cubic_bezier(u1: float, u2: float, t: float):
    return (3 * u1 * (1 - t) ** 2 * t) + (3 * u2 * (1 - t) * t**2) + t**3


def lerp(a: float, b: float, t: float):
    return (1 - t) * a + t * b


class SlideComponent(Component):
    __elapsed: float
    __duration: float

    def __init__(self):
        self.__elapsed = None
        self.__duration = None
        self.__start_x = None
        self.__end_x = None

    @property
    def active(self):
        return self.__elapsed is not None

    @property
    def done(self):
        return self.active and self.__elapsed >= self.__duration

    @property
    def progress(self):
        if not self.active:
            return None

        return self.__elapsed / self.__duration

    @property
    def start_x(self):
        return self.__start_x

    @property
    def end_x(self):
        return self.__end_x

    def get_interpolated_x(self):
        if not self.active:
            return

        t = cubic_bezier(0.8, 1, self.progress)

        return lerp(self.__start_x, self.__end_x, t)

    def reset(self):
        self.__elapsed = None
        self.__duration = None
        self.__start_x = None
        self.__end_x = None

    def set(
        self,
        start: float,
        end: float,
        duration: float,
    ):
        self.__elapsed = 0
        self.__duration = duration
        self.__start_x = start
        self.__end_x = end

    def add_progress(self, deltatime: float):
        elapsed = self.__elapsed + deltatime

        self.__elapsed = min(elapsed, self.__duration)
