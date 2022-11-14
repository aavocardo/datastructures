
def binaryMultiply(a, b):
    i, remainder, product, total = 0, 0, 0, []

    while a != 0 or b != 0:
        total.insert(i, (((a % 10) + (b % 10) + remainder) % 2))
        remainder = int(((a % 10) + (b % 10) + remainder / 2))
        a, b = int(a/10), int(b/10)
        i = i + 1

    if remainder != 0:
        total.insert(i, remainder)
        i = i + 1
    i = i - 1
    while i >= 0:
        product = (product * 10) + total[i]
        i = i - 1
    return product


print(binaryMultiply(1111, 1011))
