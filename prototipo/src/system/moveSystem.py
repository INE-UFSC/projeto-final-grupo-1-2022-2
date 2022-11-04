from ..components import MoveComponent
from .system import System


class MoveSystem(System):
    def update(self):
        ctl = self.control

        entities = ctl.entities.get_all_with(MoveComponent)

        for entity in entities:
            move = entity.get_component(MoveComponent)

            move.velocity.y += self.control.config.gravity * ctl.deltatime

            new_pos = move.pos + move.velocity * ctl.deltatime

            move.pos.update(new_pos)

            if move.pos.y < 0:
                move.pos.y = 0
                move.velocity.y = 0
