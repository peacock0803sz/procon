n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
ans = b[a[0] - 1]
for i in range(1, n):
    ans += b[a[i] - 1]
    if a[i] == a[i - 1] + 1:
        ans += c[a[i - 1] - 1]
print(ans)
