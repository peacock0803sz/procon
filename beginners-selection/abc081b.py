n = int(input())
a = (int(x) for x in input().split())
for m in range(n):
    if a % 2 == 0:
        a = a / 2
    elif a % 2 == 1:
        break
print(m)
