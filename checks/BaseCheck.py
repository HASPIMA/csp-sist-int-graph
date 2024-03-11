import abc


class BaseCheck(abc.ABC):
    check: str

    @abc.abstractmethod
    def __call__(self, *args) -> bool:
        ...

    def passes(self) -> tuple[bool, str]:
        return self(), 'Incumple' if not self() else 'Cumple'

    def __bool__(self) -> bool:
        return self()

    def __str__(self) -> str:
        _, message = self.passes()
        return f'{message} {self.check}'
