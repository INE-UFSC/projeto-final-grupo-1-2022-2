from ..components import Component
from typing import Union, Type

class Entity:
    def __init__(self, *components):
        self.__components = {
            type(component): component for component in components
        }

    def get_component(self, component_type: Type[Component]) -> Union[Component, None]:
        return self.__components.get(component_type)
        
    
    def __getitem__(self, component_type: Type[Component]):
        return self.get_component(component_type)

    @property
    def components(self):
        return self.__components