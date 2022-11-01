from .scene import Scene
from ..icontrol import IControl
from ..system import RenderSystem, MoveSystem, CameraSystem, MoveControlSystem, MapGenerationSystem, EntityDestructionSystem
from ..entity import Player



class MainScene(Scene):
    def __init__(self, control: IControl):
        menu = None
        systems = [
            MoveControlSystem(control),
            MoveSystem(control),
            CameraSystem(control),
            MapGenerationSystem(control),
            EntityDestructionSystem(control),
            RenderSystem(control),
        ]

        super().__init__(control, menu, systems)
    
    def enter(self):
        lane_i = self.control.map.lane_amount // 2
        mid_lane_x = self.control.map.lanes[lane_i]
        player = Player(pos=(mid_lane_x, 0, 0))

        self.control.entities.set_player(player)
        self.control.entities.add_entity(player)

        for system in self.systems:
            system.setup()

    def update(self):
        for system in self.systems:
            system.update()