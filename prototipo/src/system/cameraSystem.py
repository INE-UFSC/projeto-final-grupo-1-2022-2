from ..components import MoveComponent
from .system import System


class CameraSystem(System):
    def update(self):
        player = self.control.entities.player
        camera = self.control.screen.cam

        z_pos = player.get_component(MoveComponent).pos.z

        camera.update((0, z_pos))
