from checks import *
from checks.BaseCheck import BaseCheck

DIGITS = tuple(range(10))
CARRY = (0, 1)


def alldiff(*args):
    args = [a for a in args if a is not None]
    # print(args, set(args))
    return len(set(args)) == len(args)


def alldigits(*args):
    # for a in args:
    #     print(a, a in digits)
    return all(d in DIGITS or d is None for d in args)


def make_assertions(
    *,
    F: int | None = None,
    x3: int | None = None,
    x2: int | None = None,
    x1: int | None = None,

    U: int | None = None,
    R: int | None = None,

    W: int | None = None,
    T: int | None = None,

    O: int | None = None,
    should_print: bool = True,
    only_on: bool | None = None
) -> tuple[bool, list[BaseCheck]]:
    def printable(check: bool | BaseCheck, /) -> bool:
        return should_print and (only_on is None or only_on == bool(check))

    if should_print:
        print('\n{\n\t' + '_'*20,
              f'\n\t{F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}, {W=}, {T=}, {O=}')

    failed_checks: list[BaseCheck] = []

    all_true: bool = True

    all_different = alldifferent(F=F, U=U, R=R, W=W, T=T, O=O)
    all_true = all_true and all_different()

    if not all_different():
        failed_checks.append(all_different)

    if printable(all_different):
        print(f'\t\t{all_different} ->',
              f'{F=}, {U=}, {R=}, {W=}, {T=}, {O=}', all_different())

    if O is not None and\
       R is not None and\
       x1 is not None:
        if should_print:
            print('\n\t\t' + '_'*20, '\n O + O = R')

        o_remainder_inst = o_remainder(O=O, R=R,)
        all_true = all_true and o_remainder_inst()
        if not o_remainder_inst():
            failed_checks.append(o_remainder_inst)

        if printable(o_remainder_inst):
            print(f'\t\t{o_remainder_inst} ->',
                  f'(2*{O} % 10) == {R} -> {2*O % 10} == {R}', o_remainder_inst())

        o_div_inst = o_div(O=O, x1=x1)
        all_true = all_true and o_div_inst()

        if not o_div_inst():
            failed_checks.append(o_div_inst)

        if printable(o_div_inst):
            print(
                f'\t\t{o_div_inst} ->',
                f'(2*{O} // 10) == {x1} -> {2*O // 10} == {x1}',
                o_div_inst(),
            )

    if W is not None and\
            x1 is not None:

        if U is not None:
            if should_print:
                print('\n\t\t' + '_'*20, '\n W + W = U')

            w_remainder = (2*W % 10) + x1 == U
            all_true = all_true and w_remainder

            if printable(w_remainder):
                print(
                    '\t\t(2*W % 10) + x1 == U ->',
                    f'(2*{W} % 10) + {x1} == {U} -> {(2*W % 10) + x1} == {U}',
                    w_remainder,
                )

        if x2 is not None:
            w_div = (2*W + x1) // 10 == x2
            all_true = all_true and w_div
            if printable(w_div):
                print(
                    '\t\t(2*W + x1) // 10 == x2 ->',
                    f'(2*{W} + {x1}) // 10 == {x2} -> {(2*W + x1) // 10} == {x2}',
                    w_div,
                )

    if T is not None and\
            x2 is not None:
        if should_print:
            print('\n\t\t' + '_'*20, '\n T + T = FO')

        if O is not None:
            t_remainder = (2*T % 10) + x2 == O
            all_true = all_true and t_remainder
            if printable(t_remainder):
                print('\t\t(2*T % 10) + x2 == O ->',
                      f'(2*{T} % 10) + {x2} == {O} -> {(2*T % 10) + x2} == {O}', t_remainder)

        if x3 is not None:
            t_div = (2*T + x2) // 10 == x3
            all_true = all_true and t_div
            if printable(t_div):
                print('\t\t(2*T + x2) // 10 == x3 ->',
                      f'(2*{T} + {x2}) // 10 == {x3} -> {(2*T + x2) // 10} == {x3}', (2*T + x2) // 10 == x3)

    if x3 is not None and\
            F is not None:
        carry_check = F == x3
        all_true = all_true and carry_check
        if printable(carry_check):
            print('\t\tF == x3 ->', f'{F} == {x3}', F == x3)

    if should_print:
        print('\n\t' + '_'*20, f'\t{all_true= }', '}', sep='\n')
    return all_true, failed_checks


'''
NOTE: We might want to make the branches to collapse the checks into
the single most common case if any of the checks are False. This would
aid in reducing the number of nodes in the generated tree.
'''
