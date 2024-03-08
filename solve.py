from utils import make_assertions
# F = 0
x3 = 0
x2 = 0
x1 = 0

# U = 1
# R = 9

# W = 0
# T = 0

# O = 0


def solve_almost_all(*, x1: int, x2: int, x3: int):
    for U in range(10):
        for R in range(10):
            for F in range(10):
                for W in range(10):
                    for T in range(10):
                        for O in range(10):
                            if make_assertions(F=F, U=U, R=R, W=W, T=T, O=O, x1=x1, x2=x2, x3=x3, should_print=False):
                                print('++'*20,
                                      f'\n{F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}, {W=}, {T=}, {O=}')
                                make_assertions(
                                    F=F, U=U, R=R, W=W, T=T, O=O, x1=x1, x2=x2, x3=x3, should_print=True)
                                print('++'*20, end='\n\n\n')


def find_first_solution():
    nodes_visited = 0
    for U in range(10):
        if make_assertions(U=U, should_print=False):
            nodes_visited += 1
            for R in range(10):
                if make_assertions(U=U, R=R, should_print=False):
                    nodes_visited += 1
                    for F in range(10):
                        if make_assertions(U=U, R=R, F=F, should_print=False):
                            nodes_visited += 1
                            for W in range(10):
                                if make_assertions(U=U, R=R, F=F, W=W, should_print=False):
                                    nodes_visited += 1
                                    for T in range(10):
                                        if make_assertions(U=U, R=R, F=F, W=W, T=T, should_print=False):
                                            nodes_visited += 1
                                            for x1 in range(10):  # could be just 0,1
                                                if make_assertions(U=U, R=R, F=F, W=W, T=T, x1=x1, should_print=False):
                                                    nodes_visited += 1
                                                    # could be just 0,1
                                                    for x3 in range(10):
                                                        if make_assertions(U=U, R=R, F=F, W=W, T=T, x1=x1, x3=x3, should_print=False):
                                                            nodes_visited += 1
                                                            for O in range(10):
                                                                if make_assertions(U=U, R=R, F=F, W=W, T=T, x1=x1, x3=x3, O=O, should_print=False):
                                                                    nodes_visited += 1
                                                                    # could be just 0,1
                                                                    for x2 in range(10):
                                                                        if make_assertions(U=U, R=R, F=F, W=W, T=T, x1=x1, x3=x3, O=O, x2=x2, should_print=False):
                                                                            nodes_visited += 1
                                                                            print('++'*20,
                                                                                  f'\n{F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}, {W=}, {T=}, {O=}')
                                                                            make_assertions(
                                                                                F=F, U=U, R=R, W=W, T=T, O=O, x1=x1, x2=x2, x3=x3, should_print=True)
                                                                            print(
                                                                                '++'*20, end='\n\n\n')

                                                                            print(
                                                                                f'{nodes_visited=}')
                                                                            return {'U': U, 'R': R, 'F': F, 'W': W, 'T': T, 'x1': x1, 'x3': x3, 'O': O, 'x2': x2}
                                                                        else:
                                                                            print(
                                                                                f'\t//Skipping branch where {x2=}')
                                                                else:
                                                                    print(
                                                                        f'\t//Skipping branch where {O=}')
                                                        else:
                                                            print(
                                                                f'\t//Skipping branch where {x3=}')
                                                else:
                                                    print(
                                                        f'\t//Skipping branch where {x1=}')
                                        else:
                                            print(
                                                f'\t//Skipping branch where {T=}')
                                else:
                                    print(f'\t//Skipping branch where {W=}')
                        else:
                            print(f'\t//Skipping branch where {F=}')
                else:
                    print(f'\t//Skipping branch where {R=}')
        else:
            print(f'\t//Skipping branch where {U=}')


def find_less_val_less_restr() -> dict[str, int] | None:
    nodes_visited = 0
    for F in range(10):
        if make_assertions(F=F, should_print=False):
            nodes_visited += 1
            for x3 in range(10):
                if make_assertions(F=F, x3=x3, should_print=False):
                    nodes_visited += 1
                    for x2 in range(10):
                        if make_assertions(F=F, x3=x3, x2=x2, should_print=False):
                            nodes_visited += 1
                            for x1 in range(10):
                                if make_assertions(F=F, x3=x3, x2=x2, x1=x1, should_print=False):
                                    nodes_visited += 1
                                    for U in range(10):
                                        if make_assertions(F=F, x3=x3, x2=x2, x1=x1, U=U, should_print=False):
                                            nodes_visited += 1
                                            for R in range(10):  # could be just 0,1
                                                if make_assertions(F=F, x3=x3, x2=x2, x1=x1, U=U, R=R, should_print=False):
                                                    nodes_visited += 1
                                                    # could be just 0,1
                                                    for W in range(10):
                                                        if make_assertions(F=F, x3=x3, x2=x2, x1=x1, U=U, R=R, W=W, should_print=False):
                                                            nodes_visited += 1
                                                            for T in range(10):
                                                                if make_assertions(F=F, x3=x3, x2=x2, x1=x1, U=U, R=R, W=W, T=T, should_print=False):
                                                                    nodes_visited += 1
                                                                    # could be just 0,1
                                                                    for O in range(10):
                                                                        if make_assertions(F=F, x3=x3, x2=x2, x1=x1, U=U, R=R, W=W, T=T, O=O, should_print=False):
                                                                            nodes_visited += 1
                                                                            print('++'*20,
                                                                                  f'\n{F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}, {W=}, {T=}, {O=}')
                                                                            make_assertions(
                                                                                F=F, U=U, R=R, W=W, T=T, O=O, x1=x1, x2=x2, x3=x3, should_print=True)
                                                                            print(
                                                                                '++'*20, end='\n\n\n')

                                                                            print(
                                                                                f'{nodes_visited=}')
                                                                            return {'U': U, 'R': R, 'F': F, 'W': W, 'T': T, 'x1': x1, 'x3': x3, 'O': O, 'x2': x2}
                                                                        else:
                                                                            print(
                                                                                f'\t//Skipping branch where: {F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}, {W=}, {T=}, {O=}')
                                                                else:
                                                                    print(
                                                                        f'\t//Skipping branch where: {F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}, {W=}, {T=}')
                                                        else:
                                                            print(
                                                                f'\t//Skipping branch where: {F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}, {W=}')
                                                else:
                                                    print(
                                                        f'\t//Skipping branch where: {F=}, {x3=}, {x2=}, {x1=}, {U=}, {R=}')
                                        else:
                                            print(
                                                f'\t//Skipping branch where: {F=}, {x3=}, {x2=}, {x1=}, {U=}')
                                else:
                                    print(
                                        f'\t//Skipping branch where: {F=}, {x3=}, {x2=}, {x1=}')
                        else:
                            print(
                                f'\t//Skipping branch where: {F=}, {x3=}, {x2=}')
                else:
                    print(f'\t//Skipping branch where: {F=}, {x3=}')
        else:
            print(f'\t//Skipping branch where: {F=}')


def partial_solve(
    *,
    F: int,
    x3: int,
    x2: int,
    x1: int,
    U: int,
    only_on: bool | None = False,
) -> list[dict[str, int]]:
    solutions: list[dict[str, int]] = []
    iterations = 0
    for R in range(10):
        if make_assertions(F=F, U=U, R=R, x1=x1, x2=x2, x3=x3, only_on=only_on):
            iterations += 1
            for W in range(10):
                if make_assertions(F=F, U=U, R=R, W=W, x1=x1, x2=x2, x3=x3, only_on=only_on):
                    iterations += 1
                    for T in range(10):
                        if make_assertions(F=F, U=U, R=R, W=W, T=T, x1=x1, x2=x2, x3=x3, only_on=only_on):
                            iterations += 1
                            for O in range(10):
                                if make_assertions(F=F, U=U, R=R, W=W, T=T, O=O, x1=x1, x2=x2, x3=x3, only_on=only_on):
                                    iterations += 1
                                    solutions.append({
                                        'F': F,
                                        'x3': x3,
                                        'x2': x2,
                                        'x1': x1,
                                        'U': U,
                                        'R': R,
                                        'W': W,
                                        'T': T,
                                        'O': O,
                                    })

                                    print(
                                        f'[{iterations=}] found solution {solutions[-1]}')
                                else:
                                    print(f'\t//Skipping branch where {O=}')
                        else:
                            print(f'\t//Skipping branch where {T=}')
                else:
                    print(f'\t//Skipping branch where {W=}')
        else:
            print(f'\t//Skipping branch where {R=}')
    print(
        '#'*20, f'\nFound {len(solutions)} solutions in {iterations= }\n', '#'*20)
    return solutions


if __name__ == '__main__':
    import sys

    sys.stdout = open('less_val_less_restr.log', 'w')
    solution = find_less_val_less_restr()
    if solution is not None:
        for k, v in solution.items():
            print(f'{k} = {v}')
        print('++'*20)
        print(f'F = {solution["F"]}')
        print(f'x3 = {solution["x3"]}')
        print(f'x2 = {solution["x2"]}')
        print(f'x1 = {solution["x1"]}\n')

        print(f'U = {solution["U"]}')
        print(f'R = {solution["R"]}\n')

        print(f'W = {solution["W"]}')
        print(f'T = {solution["T"]}\n')

        print(f'O = {solution["O"]}')

    sys.stdout.close()
