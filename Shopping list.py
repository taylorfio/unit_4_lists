shopping_list = []
c = 1

while c == 1:
    a = input("do you want to add anything to your list?    ")  # 1 = yes and 2 = no
    if a == "1":
        b = input("what will you add?   ")
        shopping_list.append(b)
    if a == "2":
        c = c + 1


print("your list is ", shopping_list)
