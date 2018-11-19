import random
a_1list = []
a_2list = []
a_3list = []
a_4list = []
a_5list = []
a_6list = []
numlist = []


def sum_dice(dice, numrolls):
    sum = 0
    for x in range(1, numrolls):
        num_holder = random.randint(1, dice)
        sum = sum + num_holder
        numlist.append(sum)

        if sum == 1:
            return a_1list.append(1)
        if sum == 2:
            return a_2list.append(1)
        if sum == 3:
            return a_3list.append(1)
        if sum == 4:
            return a_4list.append(1)
        if sum == 5:
            return a_5list.append(1)
        if sum == 6:
            return a_6list.append(1)

    return sum


for x in range(0, 30):
   (sum_dice(6, 2))

print(numlist)

print("there are " ,(len(a_1list)), " ones")
print("there are " ,(len(a_2list)), " twos")
print("there are " ,(len(a_3list)), " threes")
print("there are " ,(len(a_4list)), " fours")
print("there are " ,(len(a_5list)), " fives")
print("there are " ,(len(a_6list)), " sixs")





