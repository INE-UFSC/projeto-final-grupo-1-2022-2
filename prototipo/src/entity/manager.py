from typing import Dict, List, Type, Union, Set
from ..components import Component
from .entity import Entity


class EntityManager:
    """Classe que contém as entidades do jogo e seus respectivos componentes"""

    __entities: Dict[Component, Set[Entity]]
    

    def __init__(self, *entities: Entity):
        self.__entities = dict()
        self.add_entity(*entities)


    def add_entity(self, *entities: Entity):
        for entity in entities:
            for component in entity.components.values():
                if type(component) not in self.__entities.keys():
                    self.__entities[type(component)] = set([entity])
                    continue

                self.__entities[type(component)].add(entity)

    def remove_entity(self, value: Entity):
        value_id = id(value)

        for entity_set in self.__entities.values():
            for entity in entity_set:
                if id(entity) == value_id:
                    entity_set.discard(entity)
                    break

    def get_all_with(self, *components: Type[Component]) -> Set[Entity]:
        """
        retorna um conjunto com todas as entidades que possuem os componentes
        inseridos. Caso não haja entidade com tal componente, retorna um conjunto vazio
        """

        returned_entities = set()
        for component in components:
            new_entities = self.__entities.get(component, returned_entities)

            if not returned_entities:
                returned_entities = new_entities
                continue
                
            returned_entities = returned_entities.intersection(new_entities)

        return returned_entities

    def get_all_entities(self) -> List[Entity]:
        returned_entities = set()

        for entity_set in self.__entities.keys:
            returned_entities.union(entity_set)

        return returned_entities 

    def clear(self):
        """
        apaga todas as entidades presentes
        """

        self.__entities.clear()

    @property
    def entities(self):
        return self.__entities
