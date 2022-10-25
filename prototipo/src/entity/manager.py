from collections import namedtuple
from typing import Dict, List, Type, Union

from ..components.Component import Component
from .entity import Entity

ComponentKey = namedtuple("ComponentKey", ["name", "id_number"])
"""
name: nome de um Component
id_number: id de uma entidade
"""


class EntityManager:
    """Classe que contém as entidades do jogo e seus respectivos componentes"""

    entities: List[Entity]
    components: Dict[ComponentKey, Component]
    """
    Em components, o valor retornado pelo dicionário é uma instância de Component pertencente à uma entidade.
    """

    def __init__(self, entities=None, components=None):
        self.__entities = [] if entities is None else entities
        self.__components = dict() if components is None else components
        self.__nextId = 0

    def generateNewId(self) -> int:
        self.__nextId += 1
        return self.__nextId - 1

    def createEntity(self, component_list: List[Component] = None) -> Entity:
        new_id = self.generateNewId()
        new_entity = Entity(new_id)

        self.__entities.append(new_entity)
        if component_list is not None:
            self.addComponentToEntity(new_entity, *component_list)

        return new_entity

    def removeEntity(self, value: Union[int, Entity]):
        """
        value: pode ser o id de uma entidade ou a própria entidade
        """

        if isinstance(value, Entity):
            value = value.id

        for i, entity in enumerate(self.__entities):
            if entity.id == value:
                self.__entities.pop(i)
                break

        for key in list(self.__components):
            if key.id_number == value:
                self.__components.pop(key)

    def addComponent(self, entity: Entity, *components: Component):
        """adiciona um ou mais componentes à uma entidade"""

        if not isinstance(entity, Entity):
            raise TypeError("primeiro parâmetro da função deve ser do tipo Entity")

        for component in components:
            if not isinstance(component, Component):
                raise TypeError(
                    f"parâmetro {component.__class__.__name__} não é do tipo Component"
                )

            key = ComponentKey(component.__class__.__name__, entity.id)
            self.__components[key] = component

    def getComponentOfEntity(
        self, entity: Entity, component: Type[Component]
    ) -> Union[Component, None]:
        """
        retorna um componente de uma entidade

        parâmetros:
        - entity: entidade que possui o componente a ser retornado
        - component: Classe do componente desejado
        """

        key = ComponentKey(component.__name__, entity.id)
        return self.__components.get(key, None)

    def getAllComponentsOfEntity(self, entity: Entity) -> List[Component]:
        """
        retorna todos os componentes de uma entidade
        parâmetros:
        - entity: entidade que possui os componentes a serem retornados
        """

        components = []

        for key, value in self.__components.items():
            if key.id_number == entity.id:
                components.append(value)
        return components

    def getEntitiesPossessingComponent(self, component: Type[Component]) -> List[int]:
        """
        retorna uma lista com os ids das entidades que contém um determinado component

        parâmetros:
        - component: Classe do componente desejado
        """

        entities = []
        for key, value in self.__components.items():
            if key.name == component.__name__:
                entities.append(key.id_number)
        return entities

    def getComponentInstances(self, component: Type[Component]) -> List[Component]:
        """
        retorna uma lista contendo todas as instâncias de um componente

        parâmetros:
        - component: Classe do componente desejado
        """

        component_list = []
        for key, value in self.__components.items():
            if key.name == component.__name__:
                component_list.append(value)
        return component_list

    def clear(self):
        """
        apaga todas as entidades presentes
        """

        self.__entities.clear()
        self.__components.clear()
