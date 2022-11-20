from ..components import CollisionComponent, MoveComponent
from ..entity import Player, Obstacle
from .system import System
from ..library import Listener


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

    @Listener.on("player_step")
    def step_over(self, player: Player, obstacle: Obstacle):
        move_player = player.get_component(MoveComponent)
        obstacle_collision = obstacle.get_component(CollisionComponent)

        obstacle_shape = obstacle_collision.shape

        move_player.pos.y = obstacle_shape.y_max
        move_player.velocity.y = 0