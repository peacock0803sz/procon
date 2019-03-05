import sys

n = int(input())
a = [int(x) for x in input().split()]

time = 0
while True:
    for m in range(n):
        if a[m] % 2 == 0:
            a[m] /= 2
        elif a[m] % 2 == 1:
            print(time)
            sys.exit()
    time += 1
