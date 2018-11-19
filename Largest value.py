inList = [1, 5, 3, 7, 4, 3, 12, 6, 8, 10, 9, 11]


def largestValue(inList):
    inList.sort()
    return inList[11]


print(largestValue(inList))
