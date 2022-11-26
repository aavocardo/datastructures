############################################################
############################################################
# binary multiply following values recursively - 1011 x 1111
############################################################
############################################################
def binary_multiply(top: int = 1011, bottom: int = 1111) -> int:
    top = list(map(int, str(top)))
    bottom = list(map(int, str(bottom)))

    remainder: int = 0
    first_product: list = []

    for bottom_ in range(1, len(bottom) + 1):
        print(bottom[-bottom_])

    for top_ in range(1, len(top) + 1):
        print(top[-top_])

    return 0


############################################################
############################################################
if __name__ == '__main__':
    # binary_multiply()

    entry1: int = 82103
    entry2: int = 69457
    binary_multiply(entry1, entry2)
