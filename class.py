
# num1 = 1011
# num1split = [int(a) for a in str(num1)]
# print(num1split)
#
# num2 = 1111
# num2split = [int(a) for a in str(num2)]
# print(num2split)

#
# def binaryMultiply(a, b):
#     a = str(a)
#     b = str(b)
#
#     result = []
#
#     for i in a:
#         j = len(b)
#         result.append(a[j] * b[i])


def binaryMultiply(a, b):
    str1, str2 = str(a), str(b)

    magic1 = str1.split()
    map_object1 = map(int, magic1)

    magic2 = str2.split()
    map_object2 = map(int, magic2)

    list1 = list(map_object1)
    list2 = list(map_object2)

    print(list1)
    print(list2)



binaryMultiply(1011, 1111)
