from .BaseCheck import BaseCheck


class o_remainder(BaseCheck):
    check = '(2*O % 10) == R'

    def __init__(self, *, O, R):
        self.O = O
        self.R = R

    def __call__(self) -> bool:
        return (2*self.O % 10) == self.R


class o_div(BaseCheck):
    check = '2*O // 10 == X1'

    def __init__(self, *, O, x1):
        self.O = O
        self.x1 = x1

    def __call__(self) -> bool:
        return (2*self.O // 10) == self.x1
