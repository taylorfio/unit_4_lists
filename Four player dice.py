import random

history = [[],[],[],[]]


def four_player_dice(dice, numrolls):
    for y in range(0, 4):
        for x in range(1, numrolls):
            num_holder = random.randint(1, dice)
            history[y].append(num_holder)


four_player_dice(6, 3)

print(history)



