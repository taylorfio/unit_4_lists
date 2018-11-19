inList = [0,1,2,3,4,5,6,7,8,9,10]

def pivotList(inList, number):
    newlist = []

    for x in inList:
        if x < number:
            newlist.append(x)
    return newlist


print(pivotList(inList, 5))