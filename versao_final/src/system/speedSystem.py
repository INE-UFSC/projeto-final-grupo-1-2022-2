from ..components import MoveComponent
from .system import System


class SpeedSystem(System):
    __time_since_last_increase: float = 0
    __time_between_increase: float = 15000
    
    def update(self):
        player = self.control.entities.player
        move = player.get_component(MoveComponent)
        
        self.__time_since_last_increase += self.control.clock.get_time()
        if self.__time_since_last_increase > self.__time_between_increase:
            self.__time_since_last_increase = 0
            move.velocity.z += 100
            self.control.event.emit("change player_velocity", move.velocity.z)