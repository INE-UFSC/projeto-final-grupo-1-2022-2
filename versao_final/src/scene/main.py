from ..entity import Player
from ..icontrol import IControl
from ..library import Listener
from ..menu import GameplayMenu
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
        menu = GameplayMenu(control)
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

        super().__init__(control, menu, systems)

    def enter(self):
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
        for system in self.systems:
            system.update()

    def render(self):
        self.menu.render()

    @Listener.on("player_collision")
    def game_over(self, player, obstacle):
        self.control.stop_running()
