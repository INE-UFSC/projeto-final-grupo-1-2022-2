from ..components import Component
from typing import Union

class Entity:
    def __init__(self, *components):
        self.__components = {
            type(component): component for component in components
        }

    def get_component(self, component: Component) -> Union[Component, None]:
        return self.__components.get(component)
        
    @property
    def components(self):
        return self.__components