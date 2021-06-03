a, b, c = int(input()), int(input()), int(input())
c2 = c**2
if a == 0:
    if b == c2:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
else:
    if c < 0:
        print('NO SOLUTION')
    else:
        x = ((c2) - b)//a
        if (x*a+b) == c2:
            print(x)
        else:
            print('NO SOLUTION')