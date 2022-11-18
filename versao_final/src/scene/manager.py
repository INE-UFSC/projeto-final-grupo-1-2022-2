from typing import Dict, Union

from .scene import Scene


class SceneManager:
    __scenes: Dict[str, Scene]
    __current_scene: Union[Scene, None]
    __next_scene: Union[Scene, None]

    def __init__(self):
        self.__scenes = {}
        self.__current_scene = None
        self.__next_scene = None

    def add(self, **scenes):
        self.__scenes.update(scenes)

    def transition(self, to_scene: Union["Scene", str, None]):
        """
        Marcar a próxima transição de cenas a ser feita na próxima vez que
        `SceneManager` atualizar. Pode-se passar tanto um objeto `Scene`
        diretamente ou seu id `str` de registro. Se `to_scene` for `None`,
        entretanto, a transição é anulada.
        """

        if to_scene is None:
            self.__next_scene = None
            return

        if isinstance(to_scene, str):
            to_scene = self.__scenes.get(to_scene)

        if isinstance(to_scene, Scene):
            self.__next_scene = to_scene

    def update_transition(self):
        """
        Aplicar transição de cenas. Esta etapa irá encerrar a atividade
        da cena atual `self.current_scene` e inicializar a próxima cena
        `self.next_scene`. Note que a cena atual pode cancelar a transição
        ou a próxima cena pode pular sua transição ou redirecioná-la se
        por acaso chamarem `SceneManager.transition` em seus métodos
        `Scene.leave` e `Scene.enter`, respectivamente.
        """

        while self.__next_scene is not None:
            current = self.__current_scene

            if current is not None:
                current.leave()

            next = self.__next_scene

            if next is not None:
                self.__current_scene = next
                self.__next_scene = None

                next.enter()

    def update(self):
        if self.__current_scene:
            self.__current_scene.update()
            self.__current_scene.render()

    @property
    def scenes(self):
        return self.__scenes

    @property
    def current_scene(self):
        return self.__current_scene

    @property
    def next_scene(self):
        return self.__next_scene
