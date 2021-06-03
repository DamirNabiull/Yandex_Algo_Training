a, b, n, m = int(input()), int(input()), int(input()), int(input())
t1 = ((n-1)*a) + n
t2 = ((m-1)*b) + m
ans1, ans2 = 0, 0

if ((t1 > t2) and ((t1-t2) > 2*b)) or ((t1 < t2) and ((t2-t1) > 2*a)):
    print(-1)
else:
    print(max(t1, t2), min(t1+2*a, t2+2*b))