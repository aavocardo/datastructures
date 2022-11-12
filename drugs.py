drugs = []


def addDrugs():
    while True:
        value = input("Input drug: ")
        drugs.append(value)
        if value == "":
            break

    def removeDrug():
        drugs.pop(0)

    def printDrugs():
        for i in drugs:
            print(drugs[i])

