from typing import Dict, List, Type, Union
from ..components import Component
from .entity import Entity


class EntityManager:
    """Classe que contém as entidades do jogo e seus respectivos componentes"""

    entities: Dict[Component, List[Entity]]
    next_id: int

    def __init__(self, *entities: Entity):
        self.__entities = dict()
        self.__next_id = 0

        self.add_entity(*entities)

    def __generate_id(self):
        self.__next_id += 1
        return self.__next_id - 1

    def add_entity(self, *entities: Entity):
        for entity in entities:
            setattr(entity, "id", self.__generate_id())
            for component in entity.components.values():
                if type(component) not in self.__entities.keys():
                    self.__entities[type(component)] = [entity]
                    continue

                self.__entities[type(component)].append(entity)

    def remove_entity(self, value: Entity):
        value_id = value.id

        for component_type, entity_list in self.__entities.items():
            for i, entity in enumerate(entity_list):
                if entity.id == value_id:
                    self.__entities[component_type].pop(i)

    def get_all_with(self, *components: Type[Component]) -> Union[List[Entity], List]:
        """
        retorna uma lista com todas as entidades que possuem os componentes
        inseridos. Caso não haja entidade com tal componente, retorna []
        """

        returned_entities = []
        id_set = set()
        for component in components:

            new_entities = self.__entities.get(component, [])
            new_ids = set([entity.id for entity in new_entities])

            if not id_set:
                id_set = new_ids
                returned_entities = new_entities
                continue

            id_set.intersection_update(new_ids)

            returned_entities = [
                entity for entity in new_entities if entity.id in id_set
            ]

        return returned_entities

    def get__all_entities(self) -> List[Entity]:
        id_list = []
        entities = []
        for entity_list in self.__entities.values():
            for entity in entity_list:
                if entity.id not in id_list:
                    entities.append(entity)
                    id_list.append(entity.id)
        return entities

    def clear(self):
        """
        apaga todas as entidades presentes
        """

        self.__entities.clear()

    @property
    def entities(self):
        return self.__entities
