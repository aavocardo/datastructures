import math
import numpy as np


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def evaluate(root):
    if root is None:
        return 0

    if root.val == '+':
        return evaluate(root.left) + evaluate(root.right)
        # addition

    elif root.val == '-':
        return evaluate(root.left) - evaluate(root.right)
        # subtraction

    elif root.val == '*':
        return evaluate(root.left) * evaluate(root.right)
        # multiplication

    elif root.val == '/':
        return evaluate(root.left) / evaluate(root.right)
        # division

    elif root.val == '**':
        return evaluate(root.left) * evaluate(root.left)
        # exponentiation

    elif root.val == 'cos':
        return math.cos(evaluate(root.left))
        # cos

    elif root.val == 'cos-1':
        return math.degrees(math.acos(evaluate(root.left)))
        # inverse cos

    elif root.val == 'sin':
        return math.sin(evaluate(root.left))
        # sin

    elif root.val == 'sin-1':
        return math.degrees(math.asin(evaluate(root.left)))
        # inverse sin

    elif root.val == 'tan':
        return math.tan(evaluate(root.left))
        # tan

    elif root.val == 'tan-1':
        return math.degrees(math.atan(evaluate(root.left)))
        # inverse tan

    elif root.val == '%':
        result = f'{evaluate(root.left) / 100}%'
        return result
        # percentage

    elif root.val == 'sqrt':
        return math.sqrt(evaluate(root.left))
        # square root

    elif root.val == 'cbrt':
        return np.cbrt(evaluate(root.left))
        # cube root

    elif root.val == '!':
        return math.factorial(evaluate(root.left))
        # factorial

    else:
        return int(root.val)


def main():
    root = Node('!')
    # input operator
    root.left = Node(9)
    root.right = Node(2)
    # input values
    result = evaluate(root)
    # call evaluate function
    print(result)


if __name__ == '__main__':
    main()
