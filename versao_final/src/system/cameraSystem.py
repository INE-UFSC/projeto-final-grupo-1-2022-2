from ..components import PosComponent
from .system import System


class CameraSystem(System):
    def update(self):
        player = self.control.entities.player
        camera = self.control.screen.cam

        z_pos = player.get_component(PosComponent).value.z

        camera.update((0, z_pos))
