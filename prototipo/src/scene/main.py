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
        player = Player()

        self.control.entities.set_player(player)
        self.control.entities.add_entity(player)

    def update(self):
        for system in self.systems:
            system.update()