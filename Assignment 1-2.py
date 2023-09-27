total_inputs = int(input("Enter the no of inputs \n"))

x=int(input("Enter a number \t"))

y=int(input("Enter a number \t"))

if y>x:

    temp=x

    x=y

    y=temp

   

for a in range(total_inputs-2):

    m=int(input("Enter a number \t"))

    if m>x and m>y and y<x:

        y=m

        temp=x

        x=y

        y=temp

    elif m>y:

        y=m

    else:

        continue

print(y)
