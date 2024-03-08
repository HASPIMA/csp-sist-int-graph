from .BaseCheck import BaseCheck


class t_remainder(BaseCheck):
    check = '(2*T % 10) + x2 == O'

    def __init__(self, *, T, x2, O):
        self.T = T
        self.x2 = x2
        self.O = O

    def __call__(self) -> bool:
        return (2*self.T % 10) + self.x2 == self.O


class t_div(BaseCheck):
    check = '(2*T + x2) // 10 == x3'

    def __init__(self, *, T, x2, x3):
        self.T = T
        self.x2 = x2
        self.x3 = x3

    def __call__(self) -> bool:
        return (2*self.T + self.x2) // 10 == self.x3


class carry_check(BaseCheck):
    check = 'F == x3'

    def __init__(self, *, F, x3):
        self.F = F
        self.x3 = x3

    def __call__(self) -> bool:
        return self.F == self.x3
