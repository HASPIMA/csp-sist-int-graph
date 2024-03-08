from .BaseCheck import BaseCheck


class w_remainder(BaseCheck):
    check = 'w_remainder'
    W: int
    U: int
    x1: int

    def __init__(self, *, W: int, U: int, x1: int):
        self.W = W
        self.U = U
        self.x1 = x1

    def __call__(self) -> bool:
        return (2*self.W % 10) + self.x1 == self.U


class w_div(BaseCheck):
    check = 'w_div'
    W: int
    x1: int
    x2: int

    def __init__(self, *, W: int, x1: int, x2: int):
        self.W = W
        self.x1 = x1
        self.x2 = x2

    def __call__(self) -> bool:
        return (2*self.W + self.x1) // 10 == self.x2
