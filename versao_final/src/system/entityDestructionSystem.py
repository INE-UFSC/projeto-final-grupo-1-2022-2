from ..components import PosComponent, RenderComponent
from .system import System


class EntityDestructionSystem(System):
    """
    Destrói as entidades que já foram
    ultrapassadas pela câmera
    """

    def update(self):
        camera = self.control.screen.cam
        destruction_distance = self.control.config.destruction_distance

        entities = self.control.entities.get_all_with(PosComponent, RenderComponent)

        for entity in entities:
            pos = entity.get_component(PosComponent).value
            size = entity.get_component(RenderComponent).size

            if pos.z + size.y < camera.pos.y - destruction_distance:
                self.control.entities.remove_entity(entity)
