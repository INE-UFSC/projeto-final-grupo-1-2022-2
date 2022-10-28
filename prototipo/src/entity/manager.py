from collections import namedtuple
from typing import Dict, List, Type, Union

from ..components import Component
from .entity import Entity


class EntityManager:
    """Classe que contém as entidades do jogo e seus respectivos componentes"""

    entities: Dict[Component, List[Entity]]



    def __init__(self, *entities: Entity):
        self.__entities = dict()

        self.add_entity(*entities)
            

    def add_entity(self, *entities: Entity):
        for entity in entities:
            for component in entity.components.values():
                if type(component) not in self.__entities.keys():
                    self.__entities[type(component)] = [entity]
                    continue

                self.__entities[type(component)].append(entity)
        

    def removeEntity(self, value: Entity):
        value_id = value.id

        for key, entity_list in self.__entities.items():
            for i, entity in enumerate(entity_list):
                if entity.id == value_id:
                    self.__entities[key].pop(i)
                    break

    def get_all_with(self, component: Component) -> Union[List[Entity], List]:
        """
        retorna uma lista com todas as entidades que possuem o componente
        inserido. Caso não haja entidade com tal componente, retorna []
        """
        
        return self.__entities.get(component, [])

    def clear(self):
        """
        apaga todas as entidades presentes
        """

        self.__entities.clear()

    @property
    def entities(self):
        return self.__entities