
class Queue:

    def __init__(self):
        self.items = []


    def push(self):
        while True:
            value = input("Input name of drug: ")
            if value == "":
                break
        self.items.append(value)


    def pop(self):
        head = self.items[0]
        self.items = self.item[1:]
        return head


    def print(self):
        for values in self.items:
            print(values)


Queue.push()