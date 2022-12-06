from ..components import CollisionComponent, PosComponent, MoveComponent
from ..entity import Player, Obstacle
from .system import System
from ..library import Listener


class MoveSystem(System):
    def update(self):
        ctl = self.control

        entities = ctl.entities.get_all_with(PosComponent, MoveComponent)

        for entity in entities:
            pos = entity.get_component(PosComponent)
            move = entity.get_component(MoveComponent)

            move.velocity.y += self.control.config.gravity * ctl.deltatime

            new_pos = pos.value + move.velocity * ctl.deltatime

            pos.value.update(new_pos)

            if pos.value.y < 0:
                pos.value.y = 0
                move.velocity.y = 0

    @Listener.on("player_step")
    def step_over(self, player: Player, obstacle: Obstacle):
        player_pos = player.get_component(PosComponent)
        player_move = player.get_component(MoveComponent)
        obstacle_collision = obstacle.get_component(CollisionComponent)

        obstacle_shape = obstacle_collision.shape

        player_pos.value.y = obstacle_shape.y_max
        player_move.velocity.y = 0