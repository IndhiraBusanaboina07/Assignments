a = int(input("Enter min number"))

b = int(input("Enter max number"))

 

for i in range(a, b+1):

    if i>1:

        for j in range(2, i):

            if (i%j) == 0:

                break

        else:

            print(i)
