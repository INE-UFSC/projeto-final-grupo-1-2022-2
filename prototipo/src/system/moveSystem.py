from .system import System
from ..components import MoveComponent
from ..icontrol import IControl

class MoveSystem(System):
    def update(self):
        ctl = self.control

        entities = ctl.entities.get_all_with(MoveComponent)

        for entity in entities:
            move = entity.get_component(MoveComponent)

            new_pos = move.pos + move.velocity * ctl.deltatime
            
            move.set_pos(new_pos)
