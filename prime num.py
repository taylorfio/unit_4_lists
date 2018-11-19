least = 1
most = 100

print("Prime numbers between",least,"and",most,"are:")

for x in range(least, most + 1):
   if x > 1:
       for i in range(2, x):
           if (x % i) == 0:
               break
       else:
           print(x)
