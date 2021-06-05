n, p, l, r = int(input()), float(input()), 30.0, 4000.0
for i in range(n-1):
    s = input().split()
    num = float(s[0])
    if num > p:
        if s[1] == 'closer':
            l = max(l, (p+num)/2)
        if s[1] == 'further':
            r = min(r, (p+num)/2)
    else:
        if s[1] == 'closer':
            r = min(r, (p+num)/2)
        if s[1] == 'further':
            l = max(l, (p+num)/2)
    p = num

print(l, r)