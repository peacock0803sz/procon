n = int(input())
h = [int(i) for i in input().split()]
check = []
if len(h) == 1:
    print('Yes')
else:
    for i in range(2, n):
        if h[i - 2] - h[i] >= 2:
            check.append(False)
        else:
            check.append(True)
    if len(set(check)) == 1:
        print('Yes')
    else:
        print('No')
