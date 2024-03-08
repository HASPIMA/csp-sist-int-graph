from .BaseCheck import BaseCheck


class o_remainder(BaseCheck):
    check = '(2*O % 10) == R'
    O: int
    R: int

    def __init__(self, *, O: int, R: int):
        self.O = O
        self.R = R

    def __call__(self) -> bool:
        return (2*self.O % 10) == self.R


class o_div(BaseCheck):
    check = '2*O // 10 == x1'
    O: int
    x1: int

    def __init__(self, *, O: int, x1: int):
        self.O = O
        self.x1 = x1

    def __call__(self) -> bool:
        return (2*self.O // 10) == self.x1
