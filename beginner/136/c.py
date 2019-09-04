n = int(input())
h = [int(i) for i in input().split()]
h[0] -= 1
if len(h) == 1:
    print('Yes')
else:
    for i in range(1, n):
        if h[i] > h[i - 1]:
            h[i] -= 1
        elif h[i] < h[i - 1]:
            print('No')
            exit()
    print('Yes')
