N, Y = map(int, input().split())
x = 0
y = 0
z = 0
if Y % 10000 == 0:
    x = Y / 10000
else:
    if Y % 5000 == 0:
        y = Y / 5000
    else:
        z = Y / 1000
if x + y + z <= N:
    print(x, y, z)
else:
    print('-1 -1 -1')
