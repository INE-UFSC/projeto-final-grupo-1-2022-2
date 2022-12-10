from .system import System
from ..components import MoveComponent, RenderComponent
from ..entity import Player
from ..library import Listener


class AnimationSystem(System):
    def update(self):
        player = self.control.entities.player
        move = player.get_component(MoveComponent)
        render = player.get_component(RenderComponent)

        render.set_duration(40 / move.velocity.z)
        if move.on_ground:
            render.set_frame("running")

    @Listener.on("player_jump")
    def jump(self, player: Player):
        render = player.get_component(RenderComponent)

        render.set_frame("jumping")
