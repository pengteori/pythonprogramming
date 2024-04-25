n = 2
s = 1

def g(n,s):
    while n <= 5:
        print(f'{n} x {s} = {n*s:2d}\t', end='')
        n += 1
        if n == 6:
            break
            n -= 4
    print()

while s <= 9:
    g(n,s)
    s += 1

n = 6
s = 1

print()

def g(n,s):
    while n <= 9:
        print(f'{n} x {s} = {n*s:2d}\t', end='')
        n += 1
        if n == 10:
            break
            n -= 4
    print()

while s <= 9:
    g(n,s)
    s += 1
    n=6
