import random


def lottery(minimum, maximum, count):
    results = [random.randint(minimum, maximum) for _ in range(count)]
    results.sort()
    return results


print(lottery(1, 42, 6))
