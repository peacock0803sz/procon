num = input().split()
k = int(num[0])
x = int(num[1])
ans = []
for i in range(x - k + 1, x + k):
    print(i)
