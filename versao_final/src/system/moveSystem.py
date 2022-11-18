from ..components import MoveComponent, CollisionComponent
from .system import System
from ..entity import Player

class MoveSystem(System):
    def update(self):
        ctl = self.control

        entities = ctl.entities.get_all_with(MoveComponent)

        for entity in entities:
            move = entity.get_component(MoveComponent)

            move.velocity.y += self.control.config.gravity * ctl.deltatime * ( 1 if not move.is_crouched else -1 )

            new_pos = move.pos + move.velocity * ctl.deltatime

            move.pos.update(new_pos)

            # zera a velocidade e a posição da entidade ao fim de um pulo ou agachamento
            if (move.pos.y < 0 and not move.is_crouched) or ( move.pos.y > 0 and move.is_crouched ):
                move.pos.y = 0
                move.velocity.y = 0
                move.is_crouched = False

            # caso a entidade possua o componente de colisão, a posição y da entidade não deve ser menor
            # que altura dela multiplicada por -1, a fim de evitar garantir que a colisão dela com outro objeto de posição y = 0
            # seja registrada
            collision = entity.get_component(CollisionComponent)
            if collision:
                height = collision.shape.size.y

                if move.pos.y <= -height:
                    move.pos.y = -height+0.1

