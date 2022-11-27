

def binary_multiply(top: int = 1011, bottom: int = 1111) -> int:
    print(top * bottom)

    results: list = []
    product: list = []
    remainder: list = []

    top = list(map(int, str(top)))
    bottom = list(map(int, str(bottom)))

    for bottom_ in range(1, len(bottom) + 1):   # 3579 x 2468
        for top_ in range(1, len(top) + 1):
            results.append(bottom[-bottom_]*top[-top_])
            # result.append(bottom[-bottom_] * top[-top_])
            # print(bottom[-bottom_]*top[-top_])

    print(results)

    for results_ in range(len(results)):
        dick = list(map(int, str(results[results_])))
        print(dick)



    if top or bottom == 0:
        return 0
    else:
        return sum(product)


def main() -> None:
    binary_multiply(3579, 2468)
    # binary_multiply()


if __name__ == '__main__':
    main()
