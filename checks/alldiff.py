from .BaseCheck import BaseCheck


class alldifferent(BaseCheck):
    check = 'alldiff'

    def __init__(self, **kwargs):
        self.this = kwargs

    def __call__(self,) -> bool:
        vals = self.this.values()
        return len(set(vals)) == len(vals)

    def __str__(self):
        _, message = self.passes()
        return f'{message} {self.check}({", ".join(self.this.keys())})'
