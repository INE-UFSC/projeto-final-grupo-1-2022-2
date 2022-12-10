from .system import System
from ..components import CollisionComponent


class CollisionSystem(System):
    def update(self):
        player = self.control.entities.player
        player_shape = player.get_component(CollisionComponent).shape

        entities = self.control.entities.get_all_with(CollisionComponent)
        entities.discard(player)

        for entity in entities:
            entity_collision = entity.get_component(CollisionComponent)

            entity_shape = entity_collision.shape
            climb_height = entity_collision.climb_height

            result = player_shape.test(entity_shape)

            if result:

                if player_shape.is_above(entity_shape, climb_height):
                    self.control.event.emit("player_step", player, entity)
                else:
                    self.control.event.emit("player_collision", player, entity)
