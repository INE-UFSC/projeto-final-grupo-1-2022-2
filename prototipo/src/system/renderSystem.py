from .system import System
from ..components import RenderComponent, MoveComponent
from ..scene import IControl

class RenderSystem(System):
    def update(self, control: IControl):
        entities = self.entities.get_all_with(RenderComponent)
        
        control.screen.fill('#0bf502')

        for entity in entities:
            render = entity.get_component(RenderComponent)
            move = entity.get_component(MoveComponent)

            if move is None:
                continue

            screen = control.screen.display

            pos = screen.get_pos(move.pos)
            screen.blit(render.surface, pos)