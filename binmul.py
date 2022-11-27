import numpy as np


def multiply(*args) -> int:
    return int(np.prod(args))


def binary_multiply(top: int = 1011, bottom: int = 1111) -> int:
    print(f'{top} x {bottom} = {top * bottom}')

    results: list = []
    product: list = []
    remainder: list = []

    top = list(map(int, str(top)))
    bottom = list(map(int, str(bottom)))

    for bottom_ in range(1, len(bottom) + 1):
        for top_ in range(1, len(top) + 1):
            temp = list(map(int, str(bottom[-bottom_] * top[-top_])))
            if len(temp) > 1:
                remainder.append(temp[0])
                temp.pop(0)
            print(temp)
            print(remainder)

    return sum(product)


def main() -> None:
    binary_multiply(3579, 2468)


if __name__ == '__main__':
    main()
