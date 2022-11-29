import numpy as np

multiply = lambda *args: np.prod(args)  # NOQA: E731
add = lambda *args: sum(args)  # NOQA: E731


def hi(name='ricardo') -> str:
    statement = 'hello'
    return f'{statement} {name}'
