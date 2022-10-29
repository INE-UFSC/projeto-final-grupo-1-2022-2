from .system import System
from ..components import RenderComponent, MoveComponent
from ..icontrol import IControl


class RenderSystem(System):
    def update(self):
        ctl = self.control
        screen = ctl.screen

        entities = ctl.entities.get_all_with(RenderComponent, MoveComponent)
        
        screen.display.fill('#0bf502')

        for entity in entities:
            render = entity.get_component(RenderComponent)
            move = entity.get_component(MoveComponent)

            pos = screen.get_pos(move.pos)
            screen.display.blit(render.surface, pos)