from typing import Callable, Generic, List, TypeVar, Union, overload

F = TypeVar("F", bound=Callable)


class ListenerFunction(Generic[F]):
    """Representa uma função que está associada a um evento."""

    def __init__(self, event_name: str, callback: F):
        self.__event_name = event_name
        self.__callback = callback

    @property
    def event_name(self) -> str:
        return self.__event_name

    @property
    def callback(self) -> F:
        return self.__callback

    def __call__(self, *args, **kwargs):
        return self.__callback(*args, **kwargs)

    def __get__(self, obj, type=None):
        if obj is None:
            return self

        return self.__callback.__get__(obj, type)


class Listener:
    """
    Classe base para objetos que recebem e emitem eventos.
    """

    __events: dict[str, list[Callable]]
    __listeners: List["Listener"]

    def __init__(self):
        self.__events = {}
        self.__listeners = []

        for name in dir(self):
            attr = getattr(type(self), name, None)

            if isinstance(attr, ListenerFunction):
                callback = getattr(self, name)
                self.subscribe(attr.event_name, callback)

    @overload
    def subscribe(self, listener: "Listener"):
        ...

    @overload
    def subscribe(self, event_name: str, callback: Callable):
        ...

    def subscribe(
        self, evt_or_listener: Union[str, "Listener"], callback: Callable = None
    ):
        """
        Inscrever a função `callback` no evento de id `evt_or_listener`. Funções
        ouvintes são chamadas quando a instância recebe o respectivo evento
        através do método `emit`.

        Também pode-se inscrever objetos `Listener` à outras instâncias de
        `Listener` a fim de emitir eventos em cadeia.

        Se `evt_or_listener` for `"*"` (wildcard), a função `callback`
        será inscrita em todos os eventos, recebendo o id do evento
        como primeiro argumento seguido por argumentos arbitrários passados
        pelo remetente do evento.
        """

        if isinstance(evt_or_listener, Listener):
            self.__listeners.append(evt_or_listener)
            return

        if callback is not None:
            subscribers = self.__events.setdefault(evt_or_listener, [])
            subscribers.append(callback)

    @overload
    def unsubscribe(self, listener: "Listener"):
        ...

    @overload
    def unsubscribe(self, event_name: str, callback: Callable):
        ...

    def unsubscribe(
        self, evt_or_listener: Union[str, "Listener"], callback: Callable = None
    ):
        if isinstance(evt_or_listener, Listener):
            if evt_or_listener in self.__listeners:
                self.__listeners.remove(evt_or_listener)

            return

        subscribers = self.__events.get(evt_or_listener, [])

        if callback in subscribers:
            subscribers.remove(callback)

    def emit(self, event_name: str, *args, **kwargs):
        """
        Emite um evento para todos os métodos ouvintes e redireciona
        o evento para Listeners inscritos.

        Parâmetros:
        - `event_name`: Identificador do evento.
        - `args` e `kwargs`: Argumentos do evento.
        """

        for callback in self.__events.get(event_name, []):
            callback(*args, **kwargs)

        for callback in self.__events.get("*", []):
            callback(event_name, *args, **kwargs)

        for listener in self.__listeners:
            listener.emit(event_name, *args, **kwargs)

    @classmethod
    def on(cls, event_name: str):
        """
        Decorador para definir um método ouvinte em uma classe. Métodos
        ouvintes são do tipo `ListenerFunction` e são automaticamente
        inscritos durante instanciação.

        ```
        class Test(Listener):
            @Listener.on("arrived")
            def greet(self, name):
                print(f"Hello, {name}")

        t = Test()
        t.emit("arrived", "Bob")
        # Hello, Bob
        ```
        """

        def decorator(f):
            return ListenerFunction(event_name, f)

        return decorator
