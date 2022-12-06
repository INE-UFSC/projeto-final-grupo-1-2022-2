import pygame as pg

from ..icontrol import IControl
from .components import Button, InputText, Text
from .layout import GridLayout
from .menu import Menu
from .render import BackgroundRender


class CreditsMenu(Menu):
    def __init__(self, control: IControl):
        
        components = [
            [Text("Corre Pro RU Créditos", font_size=64,spacing=(0,10))],
            [Text("Benedek Uzoma Kovács", font_size=24)],
            [Text("Enzo da Rosa Brum", font_size=24)],
            [Text("Joāo Pedro Schmidt Cordeiro", font_size=24)],
            [Text("William Kraus", font_size=24)],
            [Button("Return to start menu")],
            
        ]

        layout = GridLayout(
            components,
            pg.Vector2(control.screen.size),
            center_x=True,
            center_y=True,
            spacing=(50, 10),
        )

        render = BackgroundRender(control.screen, components, (0,0,0,175), layout.get_pos(), layout.get_size())

        super().__init__(control, layout, render)
