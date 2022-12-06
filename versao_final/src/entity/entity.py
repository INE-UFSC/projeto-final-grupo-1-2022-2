from typing import Type, TypeVar, Union

from ..components import Component

T = TypeVar("T", bound=Component)


class Entity:
    def __init__(self, *components):
        self.__components = {
            type(component): component
            for component in components
            if isinstance(component, Component)
        }

    def get_component(self, component_type: Type[T]) -> Union[T, None]:
        return self.__components.get(component_type)

    def set_component(self, component_type: Type[T], component: Component):
        self.__components[component_type] = component

    def __getitem__(self, component_type: Type[Component]):
        return self.get_component(component_type)

    def get_all_components(self):
        return self.__components.values()
