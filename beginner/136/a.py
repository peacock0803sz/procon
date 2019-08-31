num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])
ans = b + c - a
if ans > 0:
    print(ans)
else:
    print(0)
