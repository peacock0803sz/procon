stdin = [int(i) for i in input().split()]
n = stdin[0]
k = stdin[1]
h = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    if h[i] >= k:
        ans += 1
print(ans)
