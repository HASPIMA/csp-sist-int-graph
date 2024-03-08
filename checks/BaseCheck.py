import abc


class BaseCheck(abc.ABC):
    check: str

    @abc.abstractmethod
    def __call__(self, *args) -> bool:
        ...

    @property
    def passes(self) -> tuple[bool, str]:
        return self(), 'Incumple' if not self() else 'Cumple'

    def __str__(self) -> str:
        _, message = self.passes
        return f'{message} {self.check}'
