n = int(input())
v = [int(i) for i in input().split()]
v.sort()
ans = v[0]
for i in range(1, len(v)):
    ans = (ans + v[i]) / 2
print(ans)
