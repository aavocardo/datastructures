############################################################
############################################################
# binary multiply following values recursively - 1011 x 1111
############################################################
############################################################
def binary_multiply(top: int = 1011, bottom: int = 1111) -> int:
    result: list = []
    product: int = 0
    remainder: int = 0
    first_product: list = []
    top = list(map(int, str(top)))
    bottom = list(map(int, str(bottom)))

    for bottom_ in range(1, len(bottom) + 1):
        for top_ in range(1, len(top) + 1):
            result.append(bottom[-bottom_]*top[-top_])
            # print(bottom[-bottom_]*top[-top_])

    print(result)

    if top or bottom == 0:
        return 0
    else:
        return product


def main() -> None:
    binary_multiply(82103, 69457)
    # binary_multiply()


if __name__ == '__main__':
    main()
