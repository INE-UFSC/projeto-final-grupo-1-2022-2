from .system import System
from ..components import CollisionComponent

class CollisionSystem(System):
    def update(self):
        player = self.control.entities.player
        player_shape = player.get_component(CollisionComponent).shape

        entities = self.control.entities.get_all_with(CollisionComponent)
        entities.discard(player)

        for entity in entities:
            entity_shape = entity.get_component(CollisionComponent).shape

            result = player_shape.test(entity_shape)
            if result:
                print(result)
                self.control.stop_running()
                
