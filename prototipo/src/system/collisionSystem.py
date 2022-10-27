from .system import System
from ..components import CollisionComponent
from ..scene import IControl

class CollisionSystem(System):
    def update(self, control: IControl):
        entities = self.entities.get_all_with(CollisionComponent)

        for entity in entities:
            entity.pos += entity.velocity * control.deltatime
