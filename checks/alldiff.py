from .BaseCheck import BaseCheck


class alldifferent(BaseCheck):
    check = 'alldiff'
    this: dict[str, int | None]

    def __init__(self, **kwargs: int | None):
        self.this = kwargs

    def __call__(self,) -> bool:
        vals = [v for v in self.this.values() if v is not None]
        return len(set(vals)) == len(vals)

    def __str__(self):
        _, message = self.passes()
        return f'{message} {self.check}({", ".join(self.this.keys())})'
