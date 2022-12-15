import math
import numpy as np
import matplotlib.pyplot as plt


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, data):
        if self.left is None:
            self.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, data):
        if self.right is None:
            self.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = self.right
            self.right = new_node


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


def graph(x: list, y: list, title) -> None:
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    return None


def main1():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 9, 10]
    graph(x, y, 'graph demo')


def main2():
    # Empty stack (FIFO)
    stack = []

    # Operator input
    root = Node('*')
    # Left node input
    root.insert_left(9)
    # Right node input
    root.insert_right(3)

    stack.append(evaluate(root))
    stack.pop()

    # Result
    result = np.prod(stack)
    print(result)


if __name__ == '__main__':
    main1()

if __name__ == '__main__':
    main2()
