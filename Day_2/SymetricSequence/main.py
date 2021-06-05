import sys
n = int(input())
arr = list(map(int, input().split()))
l, r, k = 0, 0, 0

if n%2 != 0:
    l, r = n//2, n//2+1
else:
    l, r = n//2, n//2

a = arr[r:]
a.reverse()
b = arr[:l]

if a == b:
    print(0)
else:
    for i in range(n):
        k += 1
        ans = arr[:i+1]
        ans.reverse()
        temp = arr[:] + ans
        if len(temp)%2 != 0:
            l, r = len(temp) // 2, len(temp) // 2 + 1
        else:
            l, r = len(temp) // 2, len(temp) // 2

        a = temp[r:]
        a.reverse()
        b = temp[:l]

        if a == b:
            print(k)
            print(*ans)
            sys.exit()