import sys

n, yen = map(int, input().split())
for x in range(n + 1):
    for y in range(n - x + 1):
        if x * 10000 + y * 5000 + (n - x - y) * 1000 == yen:
            print(x, y, n - x - y)
            sys.exit()
print('-1 -1 -1')
