from .system import System
from ..components import MoveComponent
from ..scene import IControl

class MoveSystem(System):
    def update(self, control: IControl):
        entities = self.entities.get_all_with(MoveComponent)

        for entity in entities:
            entity.pos += entity.velocity * control.deltatime
