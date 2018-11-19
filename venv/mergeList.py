def max_list():
    list_holder = [1, 2, 3, 4, 5, 6]
    list_holder2 = [2, 4, 6, 8, 10, 12]
    list_total = []

    list3 = list_holder + list_holder2

    for x in range(len(list3)):
        list_total.insert(0, max(list3))
        list3.remove(max(list3))

    return list_total


print(max_list())