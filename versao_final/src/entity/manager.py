from typing import Dict, List, Set, Type, Union

from ..components import Component
from .entity import Entity
from .player import Player


class EntityManager:
    """Classe que contém as entidades do jogo e seus respectivos componentes"""

    __entities: Dict[Component, Set[Entity]]
    __player: Player

    def __init__(self, *entities: Entity):
        self.__entities = dict()
        self.add_entity(*entities)
        self.__player = None

    def set_player(self, player: Player):
        if isinstance(player, Player):
            self.__player = player

    def add_entity(self, *entities: Entity):
        for entity in entities:
            for component in entity.get_all_components():
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
            new_entities = self.__entities.get(component, set())

            if not returned_entities:
                returned_entities = new_entities.copy()
                continue

            returned_entities = returned_entities.intersection(new_entities)

        return returned_entities

    def get_all_entities(self) -> Set[Entity]:
        returned_entities = set()

        for entity_set in self.__entities.values():
            returned_entities = returned_entities.union(entity_set)

        return returned_entities

    def clear(self):
        """
        apaga todas as entidades presentes
        """

        self.__entities.clear()
        self.__player = None

    @property
    def entities(self):
        return self.__entities

    @property
    def player(self):
        return self.__player
