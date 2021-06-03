import sys

k1, m, k2, p2, n2 = map(int, input().split())

etazh = (p2 - 1) * m + n2

if (k2 < etazh) or (n2 > m) or (k1 <= 0) or (m <= 0) or (k2 <= 0) or (p2 <= 0) or (n2 <= 0):
    print(-1, -1)
    sys.exit()

left = (k2-1)
if etazh > 1:
    left = (k2-1)/(etazh-1)
right = (k2+1)/(etazh+1)

left = round(left) - 1000
right = round(right) + 1001

if left < 0:
    left = 1

ans = []

for i in range(left, right):
    l = i * (etazh-1)
    r = i * etazh
    if l < k2 <= r:
        ans.append(i)

if len(ans) == 0:
    print(-1, -1)
    sys.exit()

pd = []
ea = []
for i in ans:
    et = k1//i
    if k1%i > 0:
        et = et + 1
    pd.append(((et - 1) // m) + 1)
    et = et%m
    if et == 0:
        et = m
    ea.append(et)

pd = set(pd)
ea = set(ea)

if len(pd) == 1 and len(ea) == 1:
    print(pd.pop(), ea.pop())
elif len(ea) > 1 and len(pd) == 1:
    print(pd.pop(), 0)
elif len(ea) == 1 and len(pd) > 1:
    print(0, ea.pop())
else:
    print(0, 0)